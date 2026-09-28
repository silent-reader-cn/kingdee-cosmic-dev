# 定时消息任务-mbase_msgtask

## 群组消息机器人-多选基础资料表 t_mbase_msgbotbasedata

- **表名称：** 群组消息机器人-多选基础资料表
- **表名：** t_mbase_msgbotbasedata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [群消息机器人 mbase_msgbot](../mbase_files/mbase_msgbot.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mbase_msgbotbasedata |  | fpkid |
| 2 | idx_mbase_msgbotbasedata_fid |  | fid |

---

## 定时消息任务-主表 t_mbase_msgtask

- **表名称：** 定时消息任务-主表
- **表名：** t_mbase_msgtask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmobapp | 移动应用 | int8 | 64 |  | √ | 0 | [轻应用 mbase_lightapp](../mbase_files/mbase_lightapp.md) |
| 3 | finterfaceconfig | 接口详情 | int8 | 64 |  | √ | 0 | [业务接口配置 mbase_interfaceconfig](../mbase_files/mbase_interfaceconfig.md) |
| 4 | fmsgtype | 消息类型 | bpchar | 1 |  | √ | '0' | 消息类型,枚举: 0 :文本信息 1 :卡片信息 |
| 5 | ftarget | 发送目标 | bpchar | 1 |  | √ | '0' | 发送目标,枚举: 0 :群组 1 :个人 |
| 6 | fsource | 录入方式 | bpchar | 1 |  | √ | '0' | 录入方式,枚举: 0 :手工录入 1 :接口 |
| 7 | fexectime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fplandescsummary | 调度计划摘要 | varchar | 1000 |  | √ | ' ' | 调度计划摘要 |
| 11 | fbillno | 任务编码 | varchar | 30 |  | √ | ' ' | 任务编码 |
| 12 | finterfacecusparams | 接口自定义参数 | varchar | 2000 |  | √ | ' ' | 接口自定义参数 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fname | 任务名称 | varchar | 50 |  | √ | ' ' | 任务名称 |
| 15 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | fstoptype | 截止方式 | bpchar | 1 |  | √ | '0' | 截止方式,枚举: 0 :不截止 1 :截止日期 |
| 19 | fstarttime | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 20 | fcronexp | cron表达式 | varchar | 500 |  | √ | ' ' | cron表达式 |
| 21 | fmsgtitle | 消息标题 | varchar | 50 |  | √ | '0' | 消息标题 |
| 22 | furl | URL | varchar | 1000 |  | √ | ' ' | URL |
| 23 | fenable | 可用状态 | bpchar | 1 |  | √ | '1' | 可用状态,枚举: 0 :禁用 1 :启用 |
| 24 | fplantype | 计划类型 | bpchar | 1 |  | √ | '0' | 计划类型,枚举: 0 :单次计划 1 :重复计划 |
| 25 | fendtime | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 26 | fcontent | 消息内容 | varchar | 1000 |  | √ | ' ' | 消息内容 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mbase_msgtask_fbillno |  | fbillno |
| 2 | pk_mbase_msgtask |  | fid |

---

## 消息接收人-多选基础资料表 t_mbase_msgbotbaseuser

- **表名称：** 消息接收人-多选基础资料表
- **表名：** t_mbase_msgbotbaseuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mbase_msgbotbaseuser_fid |  | fid |
| 2 | pk_mbase_msgbotbaseuser |  | fpkid |
