# 工作内容-mpdm_workscopeins

## 明细信息-子表 t_mpdm_wkscope_detail

- **表名称：** 明细信息-子表
- **表名：** t_mpdm_wkscope_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailname | 名称(弃用) | varchar | 50 |  | √ | ' ' | 名称(弃用) |
| 2 | fworkdetailid | 明细id(弃用) | int8 | 64 |  | √ | 0 | 明细id(弃用) |
| 3 | fselect |  | bpchar | 1 |  | √ | '0' |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailstate | 说明(弃用) | varchar | 255 |  | √ | ' ' | 说明(弃用) |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fdetailsid | 名称 | int8 | 64 |  | √ | 0 | 工作内容明细 mpdm_workscopedetail |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_wkscope_detail |  | fdetailid |
| 2 | idx_mpdm_wkscope_detail_feq |  | fentryid,fseq |

---

## 工作内容-主表 t_mpdm_workscopeins

- **表名称：** 工作内容-主表
- **表名：** t_mpdm_workscopeins

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcontentdetail_tag | 工作内容详情_详情 | text | 0 |  | √ | ' ' | 工作内容详情_详情 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fworkscopetplid | 工作内容模板 | int8 | 64 |  | √ | 0 | 工作内容模板 mpdm_workscope |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcombotype | 组合格式 | varchar | 50 |  | √ | ' ' | 组合格式,枚举: A :类别详情 B :类别名称+类别详情 |
| 12 | fcombosymbol | 类别组合符号 | varchar | 50 |  | √ | ' ' | 类别组合符号,枚举: + :+ : :: - :- _ :_ \ :\ / :/ ~ :~ & :& |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fcontentdetail | 工作内容详情 | varchar | 255 |  | √ | ' ' | 工作内容详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_workscopeins |  | fid |
| 2 | idx_mpdm_workscopeins_fct |  | fcreatetime |
| 3 | idx_mpdm_workscopeins_fnum |  | fnumber |

---

## 工作内容明细-多选基础资料表 t_mpdm_wrokscp_detail

- **表名称：** 工作内容明细-多选基础资料表
- **表名：** t_mpdm_wrokscp_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 工作内容明细 mpdm_workscopedetail |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_wrokscp_detail_fid |  | fid |
| 2 | pk_mpdm_wrokscp_detail |  | fpkid |

---

## 工作内容-多语言表 t_mpdm_workscopeins_l

- **表名称：** 工作内容-多语言表
- **表名：** t_mpdm_workscopeins_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_workscopeins_l_fid |  | fid,flocaleid |
| 2 | pk_mpdm_workscopeins_l |  | fpkid |

---

## 工作内容类别-多选基础资料表 t_mpdm_wrokscp_cate

- **表名称：** 工作内容类别-多选基础资料表
- **表名：** t_mpdm_wrokscp_cate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 工作内容类别维护 mpdm_workcategory |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_wrokscp_cate |  | fpkid |
| 2 | idx_mpdm_wrokscp_cate_fid |  | fid |

---

## 类别信息-子表 t_mpdm_wkscope_cate

- **表名称：** 类别信息-子表
- **表名：** t_mpdm_wkscope_cate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpriority | 类别序号 | int4 | 32 |  | √ | 0 | 类别序号 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ftypedesc_tag | 类别详情_详情 | text | 0 |  | √ | ' ' | 类别详情_详情 |
| 5 | ftypedesc | 类别详情 | varchar | 255 |  | √ | ' ' | 类别详情 |
| 6 | fconnector | 明细组合符号 | varchar | 50 |  | √ | ' ' | 明细组合符号,枚举: + :+ : :: - :- _ :_ \ :\ / :/ ~ :~ & :& |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fworkcateid | 类别编码 | int8 | 64 |  | √ | 0 | 工作内容类别维护 mpdm_workcategory |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_wkscope_cate |  | fentryid |
| 2 | idx_mpdm_wkscope_cate_feq |  | fid,fseq |
