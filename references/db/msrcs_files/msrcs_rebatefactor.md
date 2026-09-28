# 返利计算指标-msrcs_rebatefactor

## 指定维度分录-子表 t_msrcs_rebatefactorde

- **表名称：** 指定维度分录-子表
- **表名：** t_msrcs_rebatefactorde

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimformula | 计算公式 | varchar | 2000 |  | √ | ' ' | 计算公式 |
| 3 | fcompareoperator | 比较符 | varchar | 10 |  | √ | ' ' | 比较符,枚举: eq :等于 bt :大于 bq :大于等于 lt :小于 lq :小于等于 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fdimension | 维度 | varchar | 80 |  | √ | ' ' | 维度,枚举: |
| 7 | fdimformuladesc | 值 | varchar | 255 |  | √ | ' ' | 值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msrcs_rebatefactorde_id |  | fid |
| 2 | pk_msrcs_rebatefactorde |  | fentryid |

---

## 返利计算指标-主表 t_msrcs_rebatefactor

- **表名称：** 返利计算指标-主表
- **表名：** t_msrcs_rebatefactor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fstatisticmethod | 函数 | bpchar | 1 |  | √ | 'A' | 函数,枚举: A :合计 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcomment | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fstatisticdimension | 统计维度 | varchar | 255 |  | √ | ' ' | 统计维度,枚举: |
| 8 | fdatasourceid | 数据源 | int8 | 64 |  | √ | 0 | [返利计算数据源 msrcs_rebatesource](../msrcs_files/msrcs_rebatesource.md) |
| 9 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 10 | ffieldkey | 字段标识 | varchar | 80 |  | √ | ' ' | 字段标识 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fformuladesc | 计算公式说明 | varchar | 255 |  | √ | ' ' | 计算公式说明 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcustomplugin | 自定义插件 | varchar | 255 |  | √ | ' ' | 自定义插件 |
| 17 | fsourcemodel | 来源计算模型 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 18 | fformula | 计算公式 | varchar | 2000 |  | √ | ' ' | 计算公式 |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_rebatefactor |  | fid |
| 2 | idx_msrcs_rebatefactor_num |  | fnumber |

---

## 返利计算指标-多语言表 t_msrcs_rebatefactor_l

- **表名称：** 返利计算指标-多语言表
- **表名：** t_msrcs_rebatefactor_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msrcs_rebatefactorl_flid |  | fid,flocaleid |
| 2 | pk_msrcs_rebatefactor_l |  | fpkid |
