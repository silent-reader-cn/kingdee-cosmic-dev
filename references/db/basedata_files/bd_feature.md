# 特征-bd_feature

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

## 特征-主表 t_bd_feature

- **表名称：** 特征-主表
- **表名：** t_bd_feature

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 特征分类 | int8 | 64 |  | √ | 0 | [特征分类 bd_featureclassfication](../basedata_files/bd_featureclassfication.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fprecision | 精度 | int4 | 32 |  | √ | 0 | 精度 |
| 5 | flength | 长度 | int4 | 32 |  | √ | 0 | 长度 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdisabletorid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fenabletorid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 12 | fisvaluemust | 特征值必录 | bpchar | 1 |  | √ | '0' | 特征值必录 |
| 13 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 14 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | foptionalconfigmethod | 选配方式 | varchar | 5 |  | √ | ' ' | 选配方式,枚举: A :单选 B :多选 |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | ffeaturetype | 特征值类型 | varchar | 5 |  | √ | ' ' | 特征值类型,枚举: A :字符 B :数值 F :辅助资料 E :布尔 |
| 19 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 特征编码 | varchar | 30 |  | √ | ' ' | 特征编码 |
| 21 | fassistantdatagroup | 辅助资料来源 | int8 | 64 |  | √ | 0 | [辅助资料分类 bos_assistantdatagroup](../base_files/bos_assistantdatagroup.md) |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_feature |  | fid |
| 2 | idx_bd_feature_fnumber |  | fnumber |

---

## 特征-多语言表 t_bd_feature_l

- **表名称：** 特征-多语言表
- **表名：** t_bd_feature_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 特征名称 | varchar | 50 |  | √ | ' ' | 特征名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_feature_l |  | fpkid |
| 2 | idx_bd_feature_l |  | fid,flocaleid |

---

## 特征值-子表 t_bd_featurevalue

- **表名称：** 特征值-子表
- **表名：** t_bd_featurevalue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryvalue | 特征值编码 | varchar | 50 |  | √ | ' ' | 特征值编码 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
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
