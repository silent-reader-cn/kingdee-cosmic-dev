# 外币换算设置-bd_exrate_config

## 单据体-子表 t_int_exruleentry

- **表名称：** 单据体-子表
- **表名：** t_int_exruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feffectivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 3 | fsourcecur | 原币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fisindirect | 使用间接汇率 | bpchar | 1 |  | √ | '1' | 使用间接汇率 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ftargetcur | 目标币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_int_exruleentry_cur_date |  | fsourcecur,ftargetcur,feffectivedate |
| 2 | pk_int_exruleentry |  | fentryid |

---

## 汇率精度单据体-子表 t_int_precision_entry

- **表名称：** 汇率精度单据体-子表
- **表名：** t_int_precision_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprecision | 汇率精度 | numeric | 23 |  | √ | 0 | 汇率精度 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fcurrency2 | 币种 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fcurrency1 | 币种 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_int_precisionentry |  | fid |
| 2 | pk_t_int_precision_entry |  | fentryid |

---

## 外币换算设置-主表 t_int_currencyexrule

- **表名称：** 外币换算设置-主表
- **表名：** t_int_currencyexrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | findirectexrate | 间接汇率 | bpchar | 1 |  | √ | '0' | 间接汇率 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 开启时间 | timestamp | 0 |  |  | null | 开启时间 |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fdefaultprecision | 全局默认精度 | varchar | 50 |  | √ | ' ' | 全局默认精度,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 |
| 7 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fexratesync | 外部汇率同步 | bpchar | 1 |  | √ | '0' | 外部汇率同步 |
| 10 | fcreatorid | 操作用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fratecontrol | 汇率修改控制 | bpchar | 1 |  | √ | '0' | 汇率修改控制 |
| 12 | fshowexratesyncentry | 自动同步源配置 | bpchar | 1 |  | √ | '0' | 自动同步源配置 |
| 13 | fshowtailzero | 补零显示 | bpchar | 1 |  | √ | '0' | 补零显示 |
| 14 | fexpirydate | 汇率失效日期 | bpchar | 1 |  | √ | '0' | 汇率失效日期 |
| 15 | fprecisioncontrol | 汇率精度控制 | bpchar | 1 |  | √ | '0' | 汇率精度控制 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_int_currencyexrule |  | fid |
| 2 | idx_int_curexrule_createtime |  | fcreatetime |

---

## 自动同步源配置单据体-子表 t_int_exratesync_entry

- **表名称：** 自动同步源配置单据体-子表
- **表名：** t_int_exratesync_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 3 | ftype | 同步规则 | varchar | 64 |  | √ | ' ' | 同步规则,枚举: 0 :每日汇率 1 :月末汇率 |
| 4 | fsnotifytype | 消息渠道 | varchar | 200 |  | √ | ' ' | 消息渠道,枚举: |
| 5 | fnotifyuser | 消息接收人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcron | cron表达式 | varchar | 64 |  | √ | ' ' | cron表达式 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdatasource | 数据源 | varchar | 64 |  | √ | ' ' | 数据源,枚举: FX_001 :人民币中间价 |
| 9 | fendtime | 同步规则失效时间 | timestamp | 0 |  |  | null | 同步规则失效时间 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fstarttime | 同步规则生效时间 | timestamp | 0 |  |  | null | 同步规则生效时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_int_exrsyn_entry |  | fid |
| 2 | pk_t_int_exratesync_entry |  | fentryid |
