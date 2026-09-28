# 工作内容模板-mpdm_workscope

## 类别信息-子表 t_mpdm_workscope_cate

- **表名称：** 类别信息-子表
- **表名：** t_mpdm_workscope_cate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpriority | 类别序号 | int4 | 32 |  | √ | 0 | 类别序号 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ftypedesc_tag | 类别详情_详情 | text | 0 |  |  | null | 类别详情_详情 |
| 5 | fconnector | 明细组合符号 | varchar | 50 |  | √ | ' ' | 明细组合符号,枚举: + :+ : :: - :- _ :_ \ :\ / :/ ~ :~ & :& |
| 6 | ftypedesc | 类别详情 | varchar | 255 |  | √ | ' ' | 类别详情 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fworkcateid | 类别编码 | int8 | 64 |  | √ | 0 | 工作内容类别维护 mpdm_workcategory |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_workscope_cate_fseq |  | fid,fseq |
| 2 | pk_mpdm_workscope_cate |  | fentryid |

---

## 工作内容模板-多语言表 t_mpdm_workscope_l

- **表名称：** 工作内容模板-多语言表
- **表名：** t_mpdm_workscope_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 工作内容名称 | varchar | 50 |  | √ | ' ' | 工作内容名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_workscope_l |  | fpkid |
| 2 | idx_mpdm_workscope_l |  | fid,flocaleid |

---

## 工作内容模板-使用范围位图表 t_mpdm_workscope_m

- **表名称：** 工作内容模板-使用范围位图表
- **表名：** t_mpdm_workscope_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_workscope_m |  | forgid |

---

## 工作内容模板-使用范围表 t_mpdm_workscope_u

- **表名称：** 工作内容模板-使用范围表
- **表名：** t_mpdm_workscope_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_workscope_u |  | fdataid,fuseorgid |
| 2 | idx_t_mpdm_workscope_u_uo |  | fuseorgid |

---

## 工作内容模板-主表 t_mpdm_workscope

- **表名称：** 工作内容模板-主表
- **表名：** t_mpdm_workscope

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcontentdetail_tag | 工作内容详情_详情 | text | 0 |  |  | null | 工作内容详情_详情 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcombotype | 组合格式 | varchar | 50 |  | √ | ' ' | 组合格式,枚举: A :类别详情 B :类别名称+类别详情 |
| 10 | fcombosymbol | 类别组合符号 | varchar | 50 |  | √ | ' ' | 类别组合符号,枚举: + :+ : :: - :- _ :_ \ :\ / :/ ~ :~ & :& |
| 11 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 16 | fname | 工作内容名称 | varchar | 50 |  | √ | ' ' | 工作内容名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | faduittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 21 | fdef | 默认模板 | bpchar | 1 |  | √ | '0' | 默认模板 |
| 22 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 工作内容编码 | varchar | 30 |  | √ | ' ' | 工作内容编码 |
| 24 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 25 | fcontentdetail | 工作内容详情 | varchar | 255 |  | √ | ' ' | 工作内容详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpdm_workscope_master |  | fmasterid |
| 2 | pk_mpdm_workscope |  | fid |
| 3 | idx_t_mpdm_workscope_createorg |  | fcreateorgid |
| 4 | idx_mpdm_workscope_fnum |  | fnumber |
| 5 | idx_mpdm_workscope_fcorg |  | fcreateorgid |
| 6 | idx_mpdm_workscope_fct |  | fcreatetime |

---

## 明细信息-子表 t_mpdm_workscope_detail

- **表名称：** 明细信息-子表
- **表名：** t_mpdm_workscope_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 2 | fstate | fstate | varchar | 255 |  | √ | ' ' |  |
| 3 | fworkdetailid | 明细id(弃用) | int8 | 64 |  | √ | 0 | 明细id(弃用) |
| 4 | fselect |  | bpchar | 1 |  | √ | '0' |  |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdetailstatus | fdetailstatus | varchar | 50 |  | √ | ' ' |  |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fdetailsid | 名称 | int8 | 64 |  | √ | 0 | 工作内容明细 mpdm_workscopedetail |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_workscope_detail |  | fdetailid |
| 2 | idx_mpdm_workscope_dl_fseq |  | fentryid,fseq |
