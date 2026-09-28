# 更新确认单F7-cad_costupdateestshf7

## 更新确认单F7-主表 t_cad_costupestbish

- **表名称：** 更新确认单F7-主表
- **表名：** t_cad_costupestbish

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftargetcosttypeid | 目标成本类型 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 3 | fstatus | fstatus | varchar | 20 |  | √ | ' ' |  |
| 4 | fsrccosttypeid | 源成本类型 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 5 | fperiodid | fperiodid | int8 | 64 |  | √ | 0 |  |
| 6 | feffecttime | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 7 | fenable | 使用状态 | varchar | 20 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 9 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_costupestbish |  | fsrccosttypeid,feffecttime |
| 2 | t_cad_costupestbish_pkey |  | fid |

---

## 更新确认单F7-多语言表 t_cad_costupestbish_l

- **表名称：** 更新确认单F7-多语言表
- **表名：** t_cad_costupestbish_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
