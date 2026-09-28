# 数据巡检计划-msbd_inspectplan

## 数据巡检计划-使用范围位图表 t_msbd_inspectplan_m

- **表名称：** 数据巡检计划-使用范围位图表
- **表名：** t_msbd_inspectplan_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwed | 星期三 | bpchar | 1 |  | √ | ' ' | 星期三 |
| 3 | fbydayorweek | 按日期或星期 | bpchar | 1 |  | √ | ' ' | 按日期或星期,枚举: d :日期 w :星期 |
| 4 | ftues | 星期二 | bpchar | 1 |  | √ | ' ' | 星期二 |
| 5 | fmar | 三月 | bpchar | 1 |  | √ | ' ' | 三月 |
| 6 | fsep | 九月 | bpchar | 1 |  | √ | ' ' | 九月 |
| 7 | foct | 十月 | bpchar | 1 |  | √ | ' ' | 十月 |
| 8 | fmay | 五月 | bpchar | 1 |  | √ | ' ' | 五月 |
| 9 | fapr | 四月 | bpchar | 1 |  | √ | ' ' | 四月 |
| 10 | fsun | 星期日 | bpchar | 1 |  | √ | ' ' | 星期日 |
| 11 | fmon | 星期一 | bpchar | 1 |  | √ | ' ' | 星期一 |
| 12 | ffri | 星期五 | bpchar | 1 |  | √ | ' ' | 星期五 |
| 13 | fjan | 一月 | bpchar | 1 |  | √ | ' ' | 一月 |
| 14 | fnov | 十一月 | bpchar | 1 |  | √ | ' ' | 十一月 |
| 15 | fnoweek | 星期几 | bpchar | 2 |  | √ | ' ' | 星期几,枚举: 1 :星期日 2 :星期一 3 :星期二 4 :星期三 5 :星期四 6 :星期五 7 :星期六 8 :自然日 9 :工作日 |
| 16 | faug | 八月 | bpchar | 1 |  | √ | ' ' | 八月 |
| 17 | fthur | 星期四 | bpchar | 1 |  | √ | ' ' | 星期四 |
| 18 | fbyweek | 星期 | bpchar | 1 |  | √ | ' ' | 星期 |
| 19 | fno | 第几个 | bpchar | 2 |  | √ | ' ' | 第几个,枚举: 1 :第一个 2 :第二个 3 :第三个 4 :第四个 5 :第五个 L :最后一个 |
| 20 | frepeatmode | 重复周期 | varchar | 10 |  | √ | ' ' | 重复周期,枚举: n :不重复 h :每小时 d :日期 w :星期 m :每月 y :每年 def :自定义 |
| 21 | fsat | 星期六 | bpchar | 1 |  | √ | ' ' | 星期六 |
| 22 | ffeb | 二月 | bpchar | 1 |  | √ | ' ' | 二月 |
| 23 | fjun | 六月 | bpchar | 1 |  | √ | ' ' | 六月 |
| 24 | fdec | 十二月 | bpchar | 1 |  | √ | ' ' | 十二月 |
| 25 | fjul | 七月 | bpchar | 1 |  | √ | ' ' | 七月 |
| 26 | fdesc | 调度计划示例 | varchar | 2000 |  | √ | ' ' | 调度计划示例 |
| 27 | fcyclenum | 重复频率 | int8 | 64 |  | √ | 0 | 重复频率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_inspectplan_m |  | fjan |
| 2 | pk_t_msbd_inspectplan_m |  | fid |

---

## 数据巡检计划-多语言表 t_msbd_inspectplan_l

- **表名称：** 数据巡检计划-多语言表
- **表名：** t_msbd_inspectplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 512 |  |  | null |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_inspectplan_l_fname |  | fname,fid |
| 2 | pk_t_msbd_inspectplan_l |  | fpkid |
| 3 | idx_msbd_inspectplan_l_fid |  | fid,flocaleid |

---

## 数据巡检计划-主表 t_msbd_inspectplan

- **表名称：** 数据巡检计划-主表
- **表名：** t_msbd_inspectplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 3 | finspectjobid | 数据巡检任务 | int8 | 64 |  | √ | 0 | 数据巡检任务 msbd_inspectjob |
| 4 | fsfailnotify | 失败 | bpchar | 1 |  | √ | '0' | 失败 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fschprincipalid | 计划负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fssuccessnotify | 成功 | bpchar | 1 |  | √ | '0' | 成功 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fareadescription | 条件描述 | varchar | 2000 |  |  | null | 条件描述 |
| 12 | fissendmsg | 巡检结果异常时是否将消息发送到消息中心 | bpchar | 1 |  | √ | '0' | 巡检结果异常时是否将消息发送到消息中心 |
| 13 | fentityid | 数据巡检维度 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 14 | fplan | cron表达式 | varchar | 300 |  | √ | ' ' | cron表达式 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 17 | fareajson | 数据范围条件json | varchar | 512 |  |  | null | 数据范围条件json |
| 18 | fscopetype | fscopetype | varchar | 5 |  | √ | ' ' |  |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fjobid | 调度作业 | varchar | 36 |  | √ | ' ' | 调度作业 sch_job |
| 21 | fareajson_tag | 数据范围条件json_详情 | text | 0 |  |  | null | 数据范围条件json_详情 |
| 22 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fdescription | fdescription | varchar | 512 |  |  | null |  |
| 24 | fstarttime | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 25 | fstimeout | 超时 | bpchar | 1 |  | √ | '0' | 超时 |
| 26 | fmsgreceiver | 消息接收人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fsmsgcontent | 消息内容 | varchar | 2000 |  |  | null | 消息内容 |
| 28 | fscheduleid | 调度计划 | varchar | 36 |  | √ | ' ' | 调度计划 sch_schedule |
| 29 | fsnotifytype | 消息渠道 | varchar | 300 |  | √ | ' ' | 消息渠道,枚举: |
| 30 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 32 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msbd_inspectplan |  | fid |
| 2 | idx_msbd_inspectplan_fnumber |  | fnumber |

---

## 数据巡检计划-分表 t_msbd_inspectplan_d

- **表名称：** 数据巡检计划-分表
- **表名：** t_msbd_inspectplan_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftwentynine | 29 | bpchar | 1 |  | √ | ' ' | 29 |
| 3 | ffour | 04 | bpchar | 1 |  | √ | ' ' | 04 |
| 4 | ftwentytwo | 22 | bpchar | 1 |  | √ | ' ' | 22 |
| 5 | ftwentyeight | 28 | bpchar | 1 |  | √ | ' ' | 28 |
| 6 | ffifteen | 15 | bpchar | 1 |  | √ | ' ' | 15 |
| 7 | ften | 10 | bpchar | 1 |  | √ | ' ' | 10 |
| 8 | fnine | 09 | bpchar | 1 |  | √ | ' ' | 09 |
| 9 | ftwentythree | 23 | bpchar | 1 |  | √ | ' ' | 23 |
| 10 | ftwentyseven | 27 | bpchar | 1 |  | √ | ' ' | 27 |
| 11 | fsix | 06 | bpchar | 1 |  | √ | ' ' | 06 |
| 12 | ftwentyfive | 25 | bpchar | 1 |  | √ | ' ' | 25 |
| 13 | fthirtyone | 31 | bpchar | 1 |  | √ | ' ' | 31 |
| 14 | fthirty | 30 | bpchar | 1 |  | √ | ' ' | 30 |
| 15 | feleven | 11 | bpchar | 1 |  | √ | ' ' | 11 |
| 16 | ffive | 05 | bpchar | 1 |  | √ | ' ' | 05 |
| 17 | ftwelve | 12 | bpchar | 1 |  | √ | ' ' | 12 |
| 18 | ffourteen | 14 | bpchar | 1 |  | √ | ' ' | 14 |
| 19 | fseventeen | 17 | bpchar | 1 |  | √ | ' ' | 17 |
| 20 | ftwo | 02 | bpchar | 1 |  | √ | ' ' | 02 |
| 21 | fthree | 03 | bpchar | 1 |  | √ | ' ' | 03 |
| 22 | fnineteen | 19 | bpchar | 1 |  | √ | ' ' | 19 |
| 23 | fthirteen | 13 | bpchar | 1 |  | √ | ' ' | 13 |
| 24 | feight | 08 | bpchar | 1 |  | √ | ' ' | 08 |
| 25 | fone | 01 | bpchar | 1 |  | √ | ' ' | 01 |
| 26 | fsixteen | 16 | bpchar | 1 |  | √ | ' ' | 16 |
| 27 | fseven | 07 | bpchar | 1 |  | √ | ' ' | 07 |
| 28 | ftwentyone | 21 | bpchar | 1 |  | √ | ' ' | 21 |
| 29 | ftwentyfour | 24 | bpchar | 1 |  | √ | ' ' | 24 |
| 30 | feighteen | 18 | bpchar | 1 |  | √ | ' ' | 18 |
| 31 | ftwentysix | 26 | bpchar | 1 |  | √ | ' ' | 26 |
| 32 | ftwenty | 20 | bpchar | 1 |  | √ | ' ' | 20 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_inspectplan_d |  | fone |
| 2 | pk_t_msbd_inspectplan_d |  | fid |
