# 调用单据配置-bdtaxr_bill_configs

## 调用单据配置-多语言表 t_bdtaxr_bill_configs_l

- **表名称：** 调用单据配置-多语言表
- **表名：** t_bdtaxr_bill_configs_l

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
| 1 | idx_bdtaxr_bill_configs_l_0 |  | fid,flocaleid |
| 2 | pk_bdtaxr_bill_configs_l |  | fpkid |

---

## 条件字段-多选基础资料表 t_bdtaxr_bill_wherefield

- **表名称：** 条件字段-多选基础资料表
- **表名：** t_bdtaxr_bill_wherefield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 条件字段 bdtaxr_where_fields |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_bill_wherefield |  | fpkid |
| 2 | idx_bdtaxr_bill_wherefield_fk |  | fid |

---

## 调用单据配置-主表 t_bdtaxr_bill_configs

- **表名称：** 调用单据配置-主表
- **表名：** t_bdtaxr_bill_configs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fbillfieldnumber | 条件字段编码 | varchar | 2000 |  | √ | ' ' | 条件字段编码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fbillfield | 条件字段名称 | varchar | 2000 |  | √ | ' ' | 条件字段名称 |
| 9 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 11 | fbillentity | 调用单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_bill_configs |  | fid |
| 2 | idx_bdtaxr_bill_configs |  | fnumber |
