# 维度-pa_dimension

## 维度-多语言表 t_pa_dimension_l

- **表名称：** 维度-多语言表
- **表名：** t_pa_dimension_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_dimension_l |  | fid,flocaleid |
| 2 | pk_t_pa_dimension_l |  | fpkid |

---

## 分析模型显示字段-子表 t_pa_dimensionentryentity

- **表名称：** 分析模型显示字段-子表
- **表名：** t_pa_dimensionentryentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldnumber | 字段编码 | varchar | 255 |  | √ | ' ' | 字段编码 |
| 3 | ffieldname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fdatatype | 数据类型 | bpchar | 1 |  | √ | ' ' | 数据类型,枚举: 0 :日期 1 :基础资料 2 :浮点型 3 :整型 4 :布尔 5 :字符 6 :上传的文件附件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_dimensionentryentity_fk |  | fid |
| 2 | pk_t_pa_dimensionentryentity |  | fentryid |

---

## 维度-主表 t_pa_dimension

- **表名称：** 维度-主表
- **表名：** t_pa_dimension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fgroupid | 字段值 | int8 | 64 |  | √ | 0 | 科目表 pa_accounttype |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fasstacttype | 关联业务维度 | int8 | 64 |  | √ | 0 | 业务维度 ai_asstacttype |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ftypefield | 类型字段 | varchar | 36 |  | √ | ' ' | 类型字段,枚举: |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fdimensiontype | 维度类型 | bpchar | 1 |  | √ | ' ' | 维度类型,枚举: 1 :基础资料类型 2 :辅助资料类型 3 :文本类型 4 :期间维度 |
| 13 | fassistantsourceid | 辅助资料来源 | int8 | 64 |  | √ | 0 | 辅助资料分类 bos_assistantdatagroup |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fdimensionsrcid | 维度来源 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 16 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 17 | fsystemid | 分析体系 | int8 | 64 |  | √ | 0 | 分析体系 pa_anasystemsetting |
| 18 | fisdefault | 是否默认预置 | bpchar | 1 |  | √ | '0' | 是否默认预置 |
| 19 | fgrouptype | 字段值类型 | varchar | 36 |  | √ | ' ' | 字段值类型,枚举: pa_accounttype :group bd_period_type :periodtype bd_accounttable :accounttable |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_dimension |  | fsystemid |
| 2 | pk_t_pa_dimension |  | fid |
| 3 | idx_pa_dimension_nbsys |  | fnumber,fsystemid |
