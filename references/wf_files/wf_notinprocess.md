# 未进入流程的单据-wf_notinprocess

## 未进入流程的单据-主表 t_wf_notinprocess

- **表名称：** 未进入流程的单据-主表
- **表名：** t_wf_notinprocess

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsubmitterid | 提单人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fsubmittime | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 4 | fentitynumber | 单据编码 | varchar | 36 |  | √ | ' ' | 单据编码 |
| 5 | fvariables | 寻址变量表 | text | 0 |  |  | null | 寻址变量表 |
| 6 | fdeadletterid | 异常流程ID | int8 | 64 |  | √ | 0 | 异常流程 wf_deadletterjob |
| 7 | foperate | 操作 | varchar | 50 |  | √ | ' ' | 操作 |
| 8 | falarmmsgsendlogid | 报警消息发送日志Id | int8 | 64 |  | √ | 0 | 报警消息发送日志Id |
| 9 | fbusinesskey | 单据ID | varchar | 36 |  | √ | ' ' | 单据ID |
| 10 | ferrorreason | 原因 | varchar | 50 |  | √ | ' ' | 原因 |
| 11 | freasonpayload | 原因负载 | text | 0 |  |  | null | 原因负载 |
| 12 | fentrabillname | 单据名称 | varchar | 255 |  | √ | ' ' | 单据名称 |
| 13 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_notinprocess_busnesskey |  | fbusinesskey,fentitynumber |
| 2 | idx_wf_notinprocess_billno |  | fbillno |
| 3 | pk_wf_notinprocess |  | fid |
| 4 | idx_wf_notinprocess_submittime |  | fsubmittime |

---

## 未进入流程的单据-多语言表 t_wf_notinprocess_l

- **表名称：** 未进入流程的单据-多语言表
- **表名：** t_wf_notinprocess_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fentrabillname | 单据名称 | varchar | 255 |  | √ | ' ' | 单据名称 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_notinprocess_l |  | fid,flocaleid |
| 2 | pk_wf_notinprocess_l |  | fpkid |
