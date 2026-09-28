# 样本与使用概率对照表-mds_samplereluse

## 样本与使用概率对照表-多语言表 t_mds_samplereluse_l

- **表名称：** 样本与使用概率对照表-多语言表
- **表名：** t_mds_samplereluse_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_samplereluse_l_id |  | fid,flocaleid |
| 2 | pk_mds_samplereluse_l |  | fpkid |

---

## 样本与使用概率对照表-主表 t_mds_samplereluse

- **表名称：** 样本与使用概率对照表-主表
- **表名：** t_mds_samplereluse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | flevelrate | 过去12个月使用频率 | int8 | 64 |  | √ | 0 | 过去12个月使用频率 |
| 5 | flevelcompare | 使用频率比较符 | varchar | 50 |  | √ | ' ' | 使用频率比较符,枚举: = := < :< <= :<= > :> >= :>= |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fprobabilitycompare | 使用概率比较符 | varchar | 50 |  | √ | ' ' | 使用概率比较符,枚举: = := < :< <= :<= > :> >= :>= |
| 8 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | flevel | 频率等级 | varchar | 50 |  | √ | ' ' | 频率等级,枚举: no movement :no movement Low :Low Medium :Medium High :High |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fprobability | 使用概率 | numeric | 23 | 10 | √ | 0 | 使用概率 |
| 13 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 15 | fsamplecompare | 样本数比较符 | varchar | 50 |  | √ | ' ' | 样本数比较符,枚举: = := < :< <= :<= > :> >= :>= |
| 16 | fsamplecount | 样本数 | int8 | 64 |  | √ | 0 | 样本数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_samplereluse |  | fcreatetime |
| 2 | pk_mds_samplereluse |  | fid |
