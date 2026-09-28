# 模板-bdtaxr_template

## 模板-主表 t_bdtaxr_template

- **表名称：** 模板-主表
- **表名：** t_bdtaxr_template

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fdata_tag | 数据_详情 | text | 0 |  |  | null | 数据_详情 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 6 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fformula | 公式 | varchar | 255 |  | √ | ' ' | 公式 |
| 10 | fissystem | 系统预置 | varchar | 50 |  | √ | ' ' | 系统预置,枚举: 0 :否 1 :是 |
| 11 | ftaxno | 税号 | varchar | 50 |  | √ | ' ' | 税号 |
| 12 | fhtml_tag | 模板html_详情 | text | 0 |  |  | null | 模板html_详情 |
| 13 | fdata | 数据 | varchar | 255 |  | √ | ' ' | 数据 |
| 14 | fissavedb | 按维度存储 | varchar | 50 |  | √ | ' ' | 按维度存储,枚举: 0 :否 1 :是 |
| 15 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 16 | fhtml | 模板html | varchar | 255 |  | √ | ' ' | 模板html |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | ftype | 模板类型 | varchar | 36 |  | √ | ' ' | [模板类型 bdtaxr_template_type](../bdtaxr_files/bdtaxr_template_type.md) |
| 20 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 21 | fcontent_tag | 模板内容_详情 | text | 0 |  |  | null | 模板内容_详情 |
| 22 | fgroup | 模板分类 | varchar | 36 |  | √ | ' ' | [模板分组 bdtaxr_template_group](../bdtaxr_files/bdtaxr_template_group.md) |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fformula_tag | 公式_详情 | text | 0 |  |  | null | 公式_详情 |
| 25 | fnumber | 模板编码 | varchar | 50 |  | √ | ' ' | 模板编码 |
| 26 | fcontent | 模板内容 | varchar | 255 |  | √ | ' ' | 模板内容 |
| 27 | fcountry | 国家或地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_template |  | fid |
| 2 | idx_bdtaxr_template |  | fnumber,fstartdate,fenddate |

---

## 模板-多语言表 t_bdtaxr_template_l

- **表名称：** 模板-多语言表
- **表名：** t_bdtaxr_template_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模板名称 | varchar | 50 |  | √ | ' ' | 模板名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_template_l_0 |  | fid,flocaleid |
| 2 | pk_bdtaxr_template_l |  | fpkid |
