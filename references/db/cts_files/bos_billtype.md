# 单据类型-bos_billtype

## 移动端字段控制-子表 t_bas_billtypefldctl_mob

- **表名称：** 移动端字段控制-子表
- **表名：** t_bas_billtypefldctl_mob

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdefaultfuncname | fdefaultfuncname | varchar | 255 |  | √ | ' ' |  |
| 3 | fvnew | 新增可见 | bpchar | 1 |  | √ | '0' | 新增可见 |
| 4 | fsysmustinput | 系统预设必录 | bpchar | 1 |  | √ | '0' | 系统预设必录 |
| 5 | fsubmitenabled | 提交锁定 | bpchar | 1 |  | √ | '0' | 提交锁定 |
| 6 | fvedit | 编辑可见 | bpchar | 1 |  | √ | '0' | 编辑可见 |
| 7 | fentityfieldkey | 实体标识 | varchar | 50 |  | √ | ' ' | 实体标识 |
| 8 | fseq | 分录行号 | int2 | 16 |  | √ | 0 | 分录行号 |
| 9 | fdefaultvaluetype | fdefaultvaluetype | int4 | 32 |  | √ | 0 |  |
| 10 | fisdeleted | 是否废弃 | bpchar | 1 |  | √ | '0' | 是否废弃 |
| 11 | feditenabled | 修改锁定 | bpchar | 1 |  | √ | '0' | 修改锁定 |
| 12 | fvaudit | 审核可见 | bpchar | 1 |  | √ | '0' | 审核可见 |
| 13 | ffieldkey | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 14 | fauditenabled | 审核锁定 | bpchar | 1 |  | √ | '0' | 审核锁定 |
| 15 | fvview | 查看可见 | bpchar | 1 |  | √ | '0' | 查看可见 |
| 16 | fmustinput | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 17 | ffieldelementtype | 字段元素类型 | int4 | 32 |  | √ | 0 | 字段元素类型 |
| 18 | fdefaultvalue | 默认值 | varchar | 255 |  | √ | ' ' | 默认值 |
| 19 | fdefaultfuncparam | 字段类型 | varchar | 100 |  | √ | ' ' | 字段类型 |
| 20 | fdefaultfuncid | fdefaultfuncid | int4 | 32 |  | √ | 0 |  |
| 21 | fvsubmit | 提交可见 | bpchar | 1 |  | √ | '0' | 提交可见 |
| 22 | fenabled | 新增锁定 | bpchar | 1 |  | √ | '0' | 新增锁定 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fvinit | 初始可见 | bpchar | 1 |  | √ | '0' | 初始可见 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bas_billtypefldctl_mob |  | fentryid |
| 2 | idx_bas_billtypefldctl_mob |  | fid |

---

## 移动端字段控制-多语言表 t_bas_billtypefldctl_mob_l

- **表名称：** 移动端字段控制-多语言表
- **表名：** t_bas_billtypefldctl_mob_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffieldname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
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
| 1 | pk_bas_billtypefldctl_mob_l |  | fpkid |
| 2 | idx_bas_billtypefldctl_mob_l |  | fentryid,flocaleid |

---

## 单据类型-主表 t_bas_billtype

- **表名称：** 单据类型-主表
- **表名：** t_bas_billtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdefwnreporttemplate | fdefwnreporttemplate | varchar | 36 |  |  | null |  |
| 3 | fbillformid | 单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | flayoutsolution | PC端布局 | varchar | 36 |  |  | null | PC端布局,枚举: |
| 5 | fdocumentstatus | fdocumentstatus | bpchar | 1 |  | √ | '0' |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fbillinitsetting | 锁定状态记录 | text | 0 |  |  | null | 锁定状态记录 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcontrolprintcount | 控制打印次数 | bpchar | 1 |  | √ | '0' | 控制打印次数 |
| 12 | fissyspreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 16 | fprintafteraudit | 审核后打印 | bpchar | 1 |  | √ | '0' | 审核后打印 |
| 17 | fmaxprintcount | 最大打印次数 | int8 | 64 |  | √ | 0 | 最大打印次数 |
| 18 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 19 | fparasettingxml | fparasettingxml | text | 0 |  |  | null |  |
| 20 | flayoutsolutionmob | 移动端布局 | varchar | 36 |  | √ | ' ' | 移动端布局,枚举: |
| 21 | fbillcoderuleid | fbillcoderuleid | varchar | 36 |  | √ | ' ' |  |
| 22 | fdefprinttemplate | 默认打印模板 | varchar | 255 |  | √ | ' ' | 默认打印模板,枚举: |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 25 | fisdefault | 默认单据类型 | bpchar | 1 |  | √ | '0' | 默认单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_billtype_pkey |  | fid |
| 2 | idx_bas_billtype |  | fbillformid,fstatus,fenable |

---

## 单据类型-多语言表 t_bas_billtype_l

- **表名称：** 单据类型-多语言表
- **表名：** t_bas_billtype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 115 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_billtype_l |  | fid,flocaleid |
| 2 | t_bas_billtype_l_pkey |  | fpkid |

---

## PC端字段控制-子表 t_bas_billtypefldctl

- **表名称：** PC端字段控制-子表
- **表名：** t_bas_billtypefldctl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdefaultfuncname | fdefaultfuncname | varchar | 255 |  | √ | ' ' |  |
| 3 | fvnew | 新增可见 | bpchar | 1 |  | √ | '0' | 新增可见 |
| 4 | fsysmustinput | 系统预设必录 | bpchar | 1 |  |  | '0' | 系统预设必录 |
| 5 | fsubmitenabled | 提交锁定 | bpchar | 1 |  | √ | '0' | 提交锁定 |
| 6 | fvedit | 编辑可见 | bpchar | 1 |  | √ | '0' | 编辑可见 |
| 7 | fentityfieldkey | 实体标识 | varchar | 50 |  | √ | ' ' | 实体标识 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fdefaultvaluetype | fdefaultvaluetype | int8 | 64 |  | √ | 0 |  |
| 10 | fisdeleted | 是否废弃 | bpchar | 1 |  | √ | '0' | 是否废弃 |
| 11 | feditenabled | 修改锁定 | bpchar | 1 |  | √ | '0' | 修改锁定 |
| 12 | fvaudit | 审核可见 | bpchar | 1 |  | √ | '0' | 审核可见 |
| 13 | ffieldkey | 字段标识 | varchar | 50 |  |  | ' ' | 字段标识 |
| 14 | fauditenabled | 审核锁定 | bpchar | 1 |  | √ | '0' | 审核锁定 |
| 15 | fvview | 查看可见 | bpchar | 1 |  | √ | '0' | 查看可见 |
| 16 | fmustinput | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 17 | ffieldelementtype | 字段元素类型 | int8 | 64 |  | √ | 0 | 字段元素类型 |
| 18 | fdefaultvalue | 默认值 | varchar | 255 |  | √ | ' ' | 默认值 |
| 19 | fdefaultfuncparam | 字段类型 | varchar | 100 |  | √ | ' ' | 字段类型 |
| 20 | fdefaultfuncid | fdefaultfuncid | int8 | 64 |  | √ | 0 |  |
| 21 | fvsubmit | 提交可见 | bpchar | 1 |  | √ | '0' | 提交可见 |
| 22 | fenabled | 新增锁定 | bpchar | 1 |  | √ | '0' | 新增锁定 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fvinit | 初始可见 | bpchar | 1 |  | √ | '0' | 初始可见 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_billtypefldctl |  | fid |
| 2 | t_bas_billtypefldctl_pkey |  | fentryid |

---

## 导出模板-多选基础资料表 t_bas_billtype_exporttpl

- **表名称：** 导出模板-多选基础资料表
- **表名：** t_bas_billtype_exporttpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [导入导出模板 bos_importtemplate](../cts_files/bos_importtemplate.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_billtype_exporttpl_pkey |  | fpkid |
| 2 | idx_bas_billtype_exporttpl_fid |  | fid |

---

## 业务流设置-子表 t_bas_billtypews

- **表名称：** 业务流设置-子表
- **表名：** t_bas_billtypews

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 3 | fbegindate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fisdefaultbf | 默认 | bpchar | 1 |  | √ | '0' | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_billtypews_pkey |  | fentryid |
| 2 | idx_bas_billtypewf |  | fid |

---

## PC端字段控制-多语言表 t_bas_billtypefldctl_l

- **表名称：** PC端字段控制-多语言表
- **表名：** t_bas_billtypefldctl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffieldname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
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
| 1 | idx_bas_billtypefldctl_l |  | fentryid,flocaleid |
| 2 | t_bas_billtypefldctl_l_pkey |  | fpkid |
| 3 | t_bas_billtypefldctl_l_fentryid_flocaleid_key |  | fentryid,flocaleid |

---

## 导入模板-多选基础资料表 t_bas_billtype_importtpl

- **表名称：** 导入模板-多选基础资料表
- **表名：** t_bas_billtype_importtpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [导入导出模板 bos_importtemplate](../cts_files/bos_importtemplate.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_billtype_importtpl_fid |  | fid |
| 2 | t_bas_billtype_importtpl_pkey |  | fpkid |
