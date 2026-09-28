# 预警配置-openapi_alarmconfig

## 消息接收人-多选基础资料表 t_openapi_alarm_receiver

- **表名称：** 消息接收人-多选基础资料表
- **表名：** t_openapi_alarm_receiver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_openapi_alarm_receiver |  | fpkid |
| 2 | idx_openapi_alarm_receiver_fk |  | fid |

---

## 预警配置-多语言表 t_openapi_alarmconfig_l

- **表名称：** 预警配置-多语言表
- **表名：** t_openapi_alarmconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_openapi_alarmconfig_fid |  | fid,flocaleid |
| 2 | pk_t_openapi_alarmconfig_l |  | fpkid |

---

## 消息渠道-多选基础资料表 t_openapi_alarm_msgtype

- **表名称：** 消息渠道-多选基础资料表
- **表名：** t_openapi_alarm_msgtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 消息渠道 msg_channel |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_openapi_alarm_msgtype |  | fpkid |
| 2 | idx_openapi_alarm_msgtype_fk |  | fid |

---

## 预警配置-主表 t_openapi_alarmconfig

- **表名称：** 预警配置-主表
- **表名：** t_openapi_alarmconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | falarmtype | 预警类型 | bpchar | 1 |  | √ | ' ' | 预警类型,枚举: 0 :慢接口 1 :API配额 2 :API熔断 3 :API安全 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | finterval | 预警间隔（分钟） | int4 | 32 |  | √ | 0 | 预警间隔（分钟） |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fmsgtitle | 标题 | varchar | 50 |  | √ | ' ' | 标题 |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 13 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 14 | fmsgtemplate | 正文 | varchar | 500 |  | √ | ' ' | 正文 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_alarmconfig_number |  | fnumber |
| 2 | pk_t_openapi_alarmconfig |  | fid |
