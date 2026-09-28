# 成本计算参数-aca_calcparam

## 成本计算参数-主表 t_aca_calcparam

- **表名称：** 成本计算参数-主表
- **表名：** t_aca_calcparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 30 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 5 | fcoprocosttypeid | fcoprocosttypeid | int8 | 64 |  | √ | 0 |  |
| 6 | freturnprocosttypeid | freturnprocosttypeid | int8 | 64 |  | √ | 0 |  |
| 7 | fcoproductrule | fcoproductrule | varchar | 60 |  | √ | ' ' |  |
| 8 | freturnprorule | 返工产品成本取数规则 | varchar | 60 |  | √ | ' ' | 返工产品成本取数规则,枚举: aca :定额成本 |
| 9 | fendwiprule | 期末在产品成本计算规则 | varchar | 60 |  | √ | ' ' | 期末在产品成本计算规则,枚举: A :计算完工成本倒挤 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_calcparam |  | fid |
| 2 | idx_aca_calcparam |  | forgid,fcostaccountid |

---

## 成本计算参数-多语言表 t_aca_calcparam_l

- **表名称：** 成本计算参数-多语言表
- **表名：** t_aca_calcparam_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_calcparam_l |  | fpkid |
| 2 | idx_aca_calcparam_l |  | fid,flocaleid |
