# 预算数据授权-xkbm_dataauth

## 预算模板单据体-子表 t_xkbm_dataauthsmp

- **表名称：** 预算模板单据体-子表
- **表名：** t_xkbm_dataauthsmp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsample | 模板编码 | varchar | 36 |  | √ | ' ' | [预算模板 xkbm_reportsample](../xkbm_files/xkbm_reportsample.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_dataauthsmp |  | fentryid |
| 2 | idx_xkbm_dauthsmp |  | fid,fsample |

---

## 预算数据授权-主表 t_xkbm_dataauth

- **表名称：** 预算数据授权-主表
- **表名：** t_xkbm_dataauth

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [预算数据授权分组 xkbm_dataauthgroup](../xkbm_files/xkbm_dataauthgroup.md) |
| 6 | fisorgunit | 预算组织 | bpchar | 1 |  | √ | ' ' | 预算组织 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fissample | 预算模板 | bpchar | 1 |  | √ | ' ' | 预算模板 |
| 9 | fnotes | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fisorgbyuser | 用户所属业务单元范围 | bpchar | 1 |  | √ | ' ' | 用户所属业务单元范围 |
| 15 | fisdimension | 预算维度 | bpchar | 1 |  | √ | ' ' | 预算维度 |
| 16 | fisscheme | 预算方案 | bpchar | 1 |  | √ | ' ' | 预算方案 |
| 17 | fisdeptbyuser | 用户所属部门范围 | bpchar | 1 |  | √ | ' ' | 用户所属部门范围 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fauthtype | 预算维度授权方式 | bpchar | 1 |  | √ | ' ' | 预算维度授权方式,枚举: 1 :维度组合授权 2 :维度交叉授权 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 21 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 22 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fpermarray | 控制功能权限项 | text | 0 |  |  | null | 控制功能权限项 |
| 24 | forgstruct | 预算组织架构 | int8 | 64 |  | √ | 0 | [预算组织架构 xkbm_budgetorg](../xkbm_files/xkbm_budgetorg.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_dataauth |  | fid |
| 2 | idx_xkbm_dataauth_num |  | fnumber |

---

## 预算数据授权-多语言表 t_xkbm_dataauth_l

- **表名称：** 预算数据授权-多语言表
- **表名：** t_xkbm_dataauth_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fnotes | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_dataauth_l |  | fid,flocaleid,fname |
| 2 | pk_xkbm_dataauth_l |  | fpkid |

---

## 预算组织单据体-子表 t_xkbm_dataauthorg

- **表名称：** 预算组织单据体-子表
- **表名：** t_xkbm_dataauthorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgunit | 组织编码 | int8 | 64 |  | √ | 0 | [预算组织选择 xkbm_orgselect](../xkbm_files/xkbm_orgselect.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_dataauthorg |  | fentryid |
| 2 | idx_xkbm_dataauthorg |  | fid,forgunit |

---

## 维度组合隐藏单据体-子表 t_xkbm_dimgroup

- **表名称：** 维度组合隐藏单据体-子表
- **表名：** t_xkbm_dimgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimensiongroup | 维度组合 | varchar | 2000 |  | √ | ' ' | 维度组合 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_ddimgrp |  | fid |
| 2 | pk_xkbm_dimgroup |  | fentryid |

---

## 预算维度二单据体-子表 t_xkbm_muldimgroup

- **表名称：** 预算维度二单据体-子表
- **表名：** t_xkbm_muldimgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimension1 | 维度1 | int8 | 64 |  | √ | 0 | 预算报表维度group xkbm_dimensiondetail |
| 3 | fdimension3 | 维度3 | int8 | 64 |  | √ | 0 | 预算报表维度group xkbm_dimensiondetail |
| 4 | fdimension2 | 维度2 | int8 | 64 |  | √ | 0 | 预算报表维度group xkbm_dimensiondetail |
| 5 | fdimension5 | 维度5 | int8 | 64 |  | √ | 0 | 预算报表维度group xkbm_dimensiondetail |
| 6 | fdimension4 | 维度4 | int8 | 64 |  | √ | 0 | 预算报表维度group xkbm_dimensiondetail |
| 7 | fdimension7 | 维度7 | int8 | 64 |  | √ | 0 | 预算报表维度group xkbm_dimensiondetail |
| 8 | fdimension6 | 维度6 | int8 | 64 |  | √ | 0 | 预算报表维度group xkbm_dimensiondetail |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fdimension8 | 维度8 | int8 | 64 |  | √ | 0 | 预算报表维度group xkbm_dimensiondetail |
| 11 | ftype8 | 类型8 | varchar | 50 |  | √ | ' ' | 类型8,枚举: xkbm_dimensiondetail :预算报表维度group |
| 12 | ftype1 | 类型1 | varchar | 50 |  | √ | ' ' | 类型1,枚举: xkbm_dimensiondetail :预算报表维度group |
| 13 | ftype3 | 类型3 | varchar | 50 |  | √ | ' ' | 类型3,枚举: xkbm_dimensiondetail :预算报表维度group |
| 14 | ftype2 | 类型2 | varchar | 50 |  | √ | ' ' | 类型2,枚举: xkbm_dimensiondetail :预算报表维度group |
| 15 | ftype5 | 类型5 | varchar | 50 |  | √ | ' ' | 类型5,枚举: xkbm_dimensiondetail :预算报表维度group |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | ftype4 | 类型4 | varchar | 50 |  | √ | ' ' | 类型4,枚举: xkbm_dimensiondetail :预算报表维度group |
| 18 | ftempfiled | 临时字段 | varchar | 50 |  | √ | ' ' | 临时字段 |
| 19 | ftype7 | 类型7 | varchar | 50 |  | √ | ' ' | 类型7,枚举: xkbm_dimensiondetail :预算报表维度group |
| 20 | ftype6 | 类型6 | varchar | 50 |  | √ | ' ' | 类型6,枚举: xkbm_dimensiondetail :预算报表维度group |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_muldimgroup |  | fentryid |
| 2 | idx_xkbm_muldimgrp |  | fid |

---

## 权限单据体-子表 t_xkbm_permitems

- **表名称：** 权限单据体-子表
- **表名：** t_xkbm_permitems

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpermcode | 权限编码 | int8 | 64 |  | √ | 0 | 权限编码 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fskillobj | 功能对象 | varchar | 255 |  | √ | ' ' | 功能对象 |
| 5 | fselected | 是否控制 | bpchar | 1 |  | √ | ' ' | 是否控制 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbizobj | 业务对象 | varchar | 255 |  | √ | ' ' | 业务对象 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_permitems |  | fid,fbizobj,fskillobj,fselected,fpermcode |
| 2 | pk_xkbm_permitems |  | fentryid |

---

## 预算维度一单据体-多语言表 t_xkbm_dataauthdimfilter_l

- **表名称：** 预算维度一单据体-多语言表
- **表名：** t_xkbm_dataauthdimfilter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdimeffect | 维度范围多语言 | varchar | 2000 |  | √ | ' ' | 维度范围多语言 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_daufilterl |  | fentryid,flocaleid |
| 2 | pk_xkbm_dataauthdimfilter_l |  | fpkid |

---

## 角色单据体-子表 t_xkbm_dataauthrole

- **表名称：** 角色单据体-子表
- **表名：** t_xkbm_dataauthrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | frolenumber | 角色编码 | varchar | 36 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_dataauthrole |  | fid,frolenumber |
| 2 | pk_xkbm_dataauthrole |  | fentryid |

---

## 预算维度一单据体-子表 t_xkbm_dataauthdimfilter

- **表名称：** 预算维度一单据体-子表
- **表名：** t_xkbm_dataauthdimfilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffiltername | 维度范围名称 | varchar | 2000 |  | √ | ' ' | 维度范围名称 |
| 3 | fseldimension | 维度 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 4 | fdimeffectdesc | 过滤条件JSON | varchar | 2000 |  | √ | ' ' | 过滤条件JSON |
| 5 | fdimeffect | 维度范围多语言 | varchar | 2000 |  | √ | ' ' | 维度范围多语言 |
| 6 | fdimeffectname | 维度过滤 | varchar | 2000 |  | √ | ' ' | 维度过滤 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ffilterkey | 维度范围Sql | varchar | 2000 |  | √ | ' ' | 维度范围Sql |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fdimeffectkey | 维度过滤条件 | varchar | 2000 |  | √ | ' ' | 维度过滤条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_daufilter |  | fid,fseldimension |
| 2 | pk_xkbm_dataauthdimfilter |  | fentryid |

---

## 用户单据体-子表 t_xkbm_dataauthuser

- **表名称：** 用户单据体-子表
- **表名：** t_xkbm_dataauthuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuserfield | 工号 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_dataauthuser |  | fentryid |
| 2 | idx_xkbm_dauthuser |  | fid,fuserfield |

---

## 预算方案单据体-子表 t_xkbm_dataauthscheme

- **表名称：** 预算方案单据体-子表
- **表名：** t_xkbm_dataauthscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fscheme | 方案编码 | int8 | 64 |  | √ | 0 | [预算方案 xkbm_scheme](../xkbm_files/xkbm_scheme.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_dataauthscheme |  | fentryid |
| 2 | idx_xkbm_dauthsch |  | fid,fscheme |

---

## 维度组合-多选基础资料表 t_xkbm_authdimensions

- **表名称：** 维度组合-多选基础资料表
- **表名：** t_xkbm_authdimensions

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_authdimensions |  | fpkid |
| 2 | idx_xkbm_authdimensions |  | fid,fbasedataid |
