# 计算公式配置-srm_cal_formula

## 计算公式配置-主表 t_pur_calformula

- **表名称：** 计算公式配置-主表
- **表名：** t_pur_calformula

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fconditionsupplierfield | 供应商字段匹配 | varchar | 100 |  | √ | ' ' | 供应商字段匹配,枚举: |
| 3 | fispreinsdata | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 4 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fconditionorderbytype | 排序方式 | varchar | 10 |  | √ | ' ' | 排序方式,枚举: desc :降序 asc :升序 |
| 10 | fformula | 总表达式 | varchar | 500 |  |  | ' ' | 总表达式 |
| 11 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 12 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fconditionfield | 取值字段 | varchar | 100 |  | √ | ' ' | 取值字段,枚举: |
| 16 | fformulapreview | 总表达式 | varchar | 1000 |  | √ | ' ' | 总表达式 |
| 17 | fconditionbillid | 取值单据 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 18 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 19 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | fconditionorderbyfield | 排序字段 | varchar | 100 |  | √ | ' ' | 排序字段,枚举: |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fcalmethod | 计算方式 | bpchar | 1 |  | √ | ' ' | 计算方式,枚举: A :公式 B :插件 C :按条件取值 |
| 24 | fpluginname | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pur_calformula |  | fid |
| 2 | idx_pur_calformula_fnumber |  | fnumber |

---

## 按条件取值-子表 t_pur_cal_condientity

- **表名称：** 按条件取值-子表
- **表名：** t_pur_cal_condientity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconditionscore | 得分 | numeric | 23 | 10 | √ | 0 | 得分 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fconditionname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fconditionid | 基础资料id | varchar | 50 |  | √ | '0' | 基础资料id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_calcondientity_fid_fseq |  | fid,fseq |
| 2 | pk_pur_cal_condientity |  | fentryid |

---

## 公式配置-子表 t_pur_calformulaentity

- **表名称：** 公式配置-子表
- **表名：** t_pur_calformulaentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forderbytype | 排序方式 | varchar | 10 |  | √ | ' ' | 排序方式,枚举: desc :降序 asc :升序 |
| 3 | forgfield | 组织字段匹配 | varchar | 50 |  | √ | ' ' | 组织字段匹配 |
| 4 | fdefaultresult | 默认得分 | numeric | 23 | 10 | √ | '-999999999' | 默认得分 |
| 5 | fgroupby | 分组 | varchar | 255 |  | √ | ' ' | 分组 |
| 6 | fevadimensionfilter | 是否按评估方式过滤 | bpchar | 1 |  | √ | 'A' | 是否按评估方式过滤,枚举: A :过滤 B :不过滤 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fsupplierfield | 供应商字段匹配 | varchar | 50 |  | √ | ' ' | 供应商字段匹配 |
| 9 | fmetadataid | 元数据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | fincludesuborg | 包含下级组织 | bpchar | 1 |  | √ | ' ' | 包含下级组织 |
| 11 | forderbyfield | 排序字段匹配 | varchar | 50 |  | √ | ' ' | 排序字段匹配 |
| 12 | fafterfiltertran | 分组后过滤器 | varchar | 1000 |  | √ | ' ' | 分组后过滤器 |
| 13 | fmaterialfield | 物料字段匹配 | varchar | 50 |  | √ | ' ' | 物料字段匹配 |
| 14 | fevalperiodfield | 评估期间字段匹配 | varchar | 50 |  | √ | ' ' | 评估期间字段匹配 |
| 15 | fchildformula | 子表达式 | varchar | 500 |  | √ | ' ' | 子表达式 |
| 16 | fafterfilter | 分组后过滤器 | varchar | 500 |  | √ | ' ' | 分组后过滤器 |
| 17 | fentitycode | 子公式编码 | varchar | 50 |  | √ | ' ' | 子公式编码 |
| 18 | fcategoryfield | 品类字段匹配 | varchar | 50 |  | √ | ' ' | 品类字段匹配 |
| 19 | fchildformulatran | 子表达式 | varchar | 1000 |  | √ | ' ' | 子表达式 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fbeforefilter | 分组前过滤器 | varchar | 500 |  | √ | ' ' | 分组前过滤器 |
| 22 | fbeforefiltertran | 分组前过滤器 | varchar | 1000 |  | √ | ' ' | 分组前过滤器 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_calformulaentity_fid_fseq |  | fid,fseq |
| 2 | pk_pur_calformulaentity |  | fentryid |

---

## 计算公式配置-多语言表 t_pur_calformula_l

- **表名称：** 计算公式配置-多语言表
- **表名：** t_pur_calformula_l

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
| 1 | pk_pur_calformula_l |  | fpkid |
| 2 | idx_pur_calformula_l_fid_flid |  | fid,flocaleid |
