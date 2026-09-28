# 成本主体级参数设置-cal_accountparamssetting

## 单据体-子表 t_cal_costaccparamsentry

- **表名称：** 单据体-子表
- **表名：** t_cal_costaccparamsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcheckornot | fcheckornot | bpchar | 1 |  | √ | '0' |  |
| 3 | fendinitcheck | 结束初始化对账是否提示 | bpchar | 1 |  | √ | '0' | 结束初始化对账是否提示,枚举: A :校验-提示 B :不校验 C :校验-强制 |
| 4 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fendaccountcheck | 结账对账是否提示 | bpchar | 1 |  | √ | '0' | 结账对账是否提示,枚举: A :校验-提示 B :不校验 C :校验-强制 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costaccparamsentry_pkey |  | fentryid |
| 2 | idx_cal_costaccpaen_costaccid |  | fcostaccountid |

---

## 成本主体级参数设置-主表 t_cal_costaccparams

- **表名称：** 成本主体级参数设置-主表
- **表名：** t_cal_costaccparams

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_costaccpa_num |  | fnumber |
| 2 | t_cal_costaccparams_pkey |  | fid |
