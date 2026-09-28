# 特征定义-pdm_featuredefinition

## 特征值-子表 t_pdm_featurevalue

- **表名称：** 特征值-子表
- **表名：** t_pdm_featurevalue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryvalue | 特征值 | varchar | 50 |  | √ | ' ' | 特征值 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 5 | fisdefaultvalue | 首选 | bpchar | 1 |  | √ | '0' | 首选 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryvaluename | 特征值名称 | varchar | 50 |  | √ | ' ' | 特征值名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_featue_fid |  | fid |
| 2 | pk_pdm_featurevalue |  | fentryid |
| 3 | idx_pdm_featue_fseq |  | fseq |

---

## 特征定义-多语言表 t_pdm_featuredefinition_l

- **表名称：** 特征定义-多语言表
- **表名：** t_pdm_featuredefinition_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_featuredefinition_l |  | fpkid |
| 2 | idx_pdm_featonl_fid |  | fid,flocaleid |
| 3 | idx_pdm_featonl_fname |  | fname |

---

## 特征定义-主表 t_pdm_featuredefinition

- **表名称：** 特征定义-主表
- **表名：** t_pdm_featuredefinition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fgroupid | 特征组 | int8 | 64 |  | √ | 0 | [特征组 pdm_featuredefgroup](../pdm_files/pdm_featuredefgroup.md) |
| 4 | fisvalueshow | 特征值显示 | bpchar | 1 |  | √ | '1' | 特征值显示 |
| 5 | fprecision | 精度 | int8 | 64 |  | √ | 0 | 精度 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | flength | 长度 | int8 | 64 |  | √ | 0 | 长度 |
| 8 | fdisabletorid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | ffieldname | 字段名 | varchar | 50 |  | √ | ' ' | 字段名 |
| 10 | fentityobjectid | 业务对象 | varchar | 255 |  | √ | '0' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fenabletorid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 15 | fisvaluemust | 特征值必录 | bpchar | 1 |  | √ | '1' | 特征值必录 |
| 16 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 17 | fstatus | 数据状态 | varchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 20 | ffeaturetype | 特征值类型 | varchar | 5 |  | √ | ' ' | 特征值类型,枚举: A :字符 B :数值 C :辅助属性 D :业务对象 E :布尔 |
| 21 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | [辅助属性定义 bd_auxproperty](../sbd_files/bd_auxproperty.md) |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_featon_fcreatetime |  | fcreatetime |
| 2 | idx_pdm_featon_fnumber |  | fnumber |
| 3 | pk_pdm_featuredefinition |  | fid |
