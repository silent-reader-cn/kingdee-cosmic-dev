# 特征值-bd_featurevalue

## 特征值-多语言表 t_bd_featurevalue_l

- **表名称：** 特征值-多语言表
- **表名：** t_bd_featurevalue_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fentryvaluename | 特征值名称 | varchar | 80 |  | √ | ' ' | 特征值名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_featurevalue_l |  | fentryid,flocaleid |
| 2 | pk_bd_featurevalue_l |  | fpkid |

---

## 特征值-主表 t_bd_featurevalue

- **表名称：** 特征值-主表
- **表名：** t_bd_featurevalue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 特征主键 | int8 | 64 |  | √ | 0 | 特征主键 |
| 2 | fentryvalue | 特征值编码 | varchar | 50 |  | √ | ' ' | 特征值编码 |
| 3 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 4 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 5 | fentryfeaturetype | 特征值类型 | varchar | 5 |  | √ | ' ' | 特征值类型,枚举: A :字符 B :数值 F :辅助资料 E :布尔 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryassistantdatadetail | 辅助资料 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_featurevalue_fid |  | fid,fentryid |
| 2 | pk_bd_featurevalue |  | fentryid |
