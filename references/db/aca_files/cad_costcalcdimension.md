# 成本核算维度-cad_costcalcdimension

## 成本核算维度-主表 t_cad_costcalcdimension

- **表名称：** 成本核算维度-主表
- **表名：** t_cad_costcalcdimension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 10 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | flevel | 优先级 | varchar | 50 |  | √ | '1' | 优先级,枚举: 1 :一级 2 :二级 3 :三级 4 :四级 5 :五级 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fpreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 11 | fenable | 使用状态 | varchar | 10 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 13 | fcalcrule | 核算维度 | varchar | 255 |  | √ | ' ' | 核算维度,枚举: YDDH :源单单号 YDHH :源单行号 CP :产品 XMH :项目号 GZH :跟踪号 PZH :配置号 SCBH :生产编号 SCX :生产线 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_costcalcdimension |  | fid |
| 2 | idx_cad_costcalcdimension_0 |  | fstatus |
| 3 | idx_cad_costcalcdimension |  | fpreset |

---

## 单据体-子表 t_cad_costdimentry

- **表名称：** 单据体-子表
- **表名：** t_cad_costdimentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 3 | ffield | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_costdimentry |  | fid |
| 2 | pk_t_cad_costdimentry |  | fentryid |

---

## 成本核算维度-多语言表 t_cad_costcalcdimension_l

- **表名称：** 成本核算维度-多语言表
- **表名：** t_cad_costcalcdimension_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_costcalcdimension_l |  | fpkid |
| 2 | idx_cad_costcalcdimension_l |  | fid,flocaleid |
