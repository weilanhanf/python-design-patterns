#!/user/bin/env python
# -*- coding: utf-8 -*-

#实现抽象的状态类
class LiftState:
    def open(self):
        pass
    def close(self):
        pass
    def run(self):
        pass
    def stop(self):
        pass

#实现各个具体的状态类
class OpenState(LiftState):
    def open(self):
        print("OPEN:The door is opened...")
        return self
    def close(self):
        print("OPEN:The door start to close...")
        print("OPEN:The door is closed")
        return StopState()
    def run(self):
        print("OPEN:Run Forbidden.")
        return self
    def stop(self):
        print("OPEN:Stop Forbidden.")
        return self
class RunState(LiftState):
    def open(self):
        print("RUN:Open Forbidden.")
        return self
    def close(self):
        print("RUN:Close Forbidden.")
        return self
    def run(self):
        print("RUN:The lift is running...")
        return self
    def stop(self):
        print("RUN:The lift start to stop...")
        print("RUN:The lift stopped...")
        return StopState()
class StopState(LiftState):
    def open(self):
        print("STOP:The door is opening...")
        print("STOP:The door is opened...")
        return OpenState()
    def close(self):
        print("STOP:Close Forbidden")
        return self
    def run(self):
        print("STOP:The lift start to run...")
        return RunState()
    def stop(self):
        print("STOP:The lift is stopped.")
        return self

#为在业务中调度状态转移，还需要将上下文进行记录，需要一个上下文的类
class Context:
    lift_state=""
    def getState(self):
        return self.lift_state
    def setState(self,lift_state):
        self.lift_state=lift_state
    def open(self):
        self.setState(self.lift_state.open())
    def close(self):
        self.setState(self.lift_state.close())
    def run(self):
        self.setState(self.lift_state.run())
    def stop(self):
        self.setState(self.lift_state.stop())

#这样，在进行电梯的调度时，只需要调度Context就可以了。业务逻辑中如下
if __name__=="__main__":
    ctx = Context()
    ctx.setState(StopState())
    ctx.open()
    ctx.run()
    ctx.close()
    ctx.run()
    ctx.stop()