# 语义规则配置-mai_sercfg

## 语义规则配置-主表 t_mai_sercfg

- **表名称：** 语义规则配置-主表
- **表名：** t_mai_sercfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 业务名词 | varchar | 100 |  | √ | ' ' | 业务名词 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fruletype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: 0 :语义转换 1 :规则约束 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fenable | 可用状态 | varchar | 50 |  | √ | '1' | 可用状态,枚举: 0 :禁用 1 :启用 |
| 11 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 12 | fdesc | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 13 | fsynonyms | 近义词 | varchar | 100 |  | √ | ' ' | 近义词 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mai_sercfg_fname |  | fname |
| 2 | pk_t_mai_sercfg |  | fid |

---

## 语义规则配置-多语言表 t_mai_sercfg_l

- **表名称：** 语义规则配置-多语言表
- **表名：** t_mai_sercfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 业务名词 | varchar | 100 |  | √ | ' ' | 业务名词 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mai_sercfg_l |  | fpkid |
| 2 | idx_mai_sercfg_l_0 |  | fid,flocaleid |
