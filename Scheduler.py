# 定时周期启动(间隔时间为1分钟)
scheduler = BlockingScheduler(timezone='Asia/Shanghai')
scheduler.add_job(
    func=self.monitor,
    trigger='interval',
    minutes=self.time_span,
    next_run_time=datetime.now(),

)
scheduler.start()

# 定时启动(每个整点)
scheduler = BlockingScheduler(timezone='Asia/Shanghai')
scheduler.add_job(
    func=self.sfc.intel_forec_main,
    trigger='cron',
    minute=0,
    next_run_time=datetime.now()
)
scheduler.start()
