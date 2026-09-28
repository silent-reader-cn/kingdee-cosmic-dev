# 标准成本卷算参数-cad_calcparameter

## 标准成本卷算参数-主表 t_cad_calcparameter

- **表名称：** 标准成本卷算参数-主表
- **表名：** t_cad_calcparameter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisyield | 是否考虑成品率 | bpchar | 1 |  | √ | ' ' | 是否考虑成品率 |
| 3 | fismateffecdate | 是否考虑物料有效期 | bpchar | 1 |  | √ | '0' | 是否考虑物料有效期 |
| 4 | fispreparhour | 是否考虑准备工时 | bpchar | 1 |  | √ | '0' | 是否考虑准备工时 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fislossrate | 是否考虑损耗率 | bpchar | 1 |  | √ | '0' | 是否考虑损耗率 |
| 7 | fiscurlevel | 是否只考虑本层次 | bpchar | 1 |  | √ | '0' | 是否只考虑本层次 |
| 8 | fcalcdate | 卷算日期 | timestamp | 0 |  |  | null | 卷算日期 |
| 9 | fcosttypeid | 成本类型 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 10 | fselematmodle | 指定物料方式 | varchar | 30 |  | √ | ' ' | 指定物料方式,枚举: 1 :物料 2 :物料组 |
| 11 | fisselectedmat | 是否指定物料 | bpchar | 1 |  | √ | '0' | 是否指定物料 |
| 12 | fisselectedbom | 是否制定bom | bpchar | 1 |  | √ | '0' | 是否制定bom |
| 13 | ftaskid | 文本 | varchar | 100 |  | √ | ' ' | 文本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_calcparameter_pkey |  | fid |

---

## 单据体-子表 t_cad_calcparammatgroup

- **表名称：** 单据体-子表
- **表名：** t_cad_calcparammatgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialgroupid | 物料组 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_calcparammatgroup_pkey |  | fentryid |

---

## 单据体-子表 t_cad_calcparammat

- **表名称：** 单据体-子表
- **表名：** t_cad_calcparammat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fmatvers | 版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | [辅助属性定义 bd_auxproperty](../sbd_files/bd_auxproperty.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_calcparammat_pkey |  | fentryid |
