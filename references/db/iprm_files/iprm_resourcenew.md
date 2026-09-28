# 云内容-iprm_resourcenew

## 单据体-子表 t_iprm_resource_entry

- **表名称：** 单据体-子表
- **表名：** t_iprm_resource_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcenumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 3 | fsourcetype | 业务对象标识 | varchar | 100 |  | √ | ' ' | 业务对象标识 |
| 4 | fsourcename | 文件名称 | varchar | 100 |  | √ | ' ' | 文件名称 |
| 5 | fbusinessobject | 业务对象名称 | varchar | 100 |  | √ | ' ' | 业务对象名称 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iprm_resource_entry |  | fid |
| 2 | idx_iprm_resource_entry_name |  | fsourcename |

---

## 云内容-主表 t_iprm_resource

- **表名称：** 云内容-主表
- **表名：** t_iprm_resource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdomain | 领域 | varchar | 50 |  | √ | ' ' | 领域 |
| 3 | fcreate_org | 创作组织 | varchar | 50 |  | √ | ' ' | 创作组织 |
| 4 | fattachmenturl | 附件路径 | varchar | 255 |  | √ | ' ' | 附件路径 |
| 5 | frtype | 内容包类型 | int8 | 64 |  | √ | 0 | [行业 iprm_res_rtype](../iprm_files/iprm_res_rtype.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fpicture | 图片字段 | varchar | 255 |  | √ | ' ' | 图片字段 |
| 8 | fcreatedate | 创作日期 | timestamp | 0 |  |  | null | 创作日期 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fre_score | 资源分数 | numeric | 23 | 10 | √ | 0 | 资源分数 |
| 11 | fsupportlangtype | 四级支持语言 | int8 | 64 |  | √ | 0 | [支持语言 iprm_res_supportlang](../iprm_files/iprm_res_supportlang.md) |
| 12 | findustry | 行业 | varchar | 100 |  | √ | ' ' | 行业 |
| 13 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 14 | fversion | 版本 | varchar | 100 |  | √ | ' ' | 版本 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fcontenttype | 内容类型 | varchar | 2 |  | √ | ' ' | 内容类型,枚举: 4 : |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | ftypename | 分类 | varchar | 100 |  | √ | ' ' | 分类 |
| 22 | fttype | 三级分类 | int8 | 64 |  | √ | 0 | [主题 iprm_res_ttype](../iprm_files/iprm_res_ttype.md) |
| 23 | fitype | 二级分类 | int8 | 64 |  | √ | 0 | [领域 iprm_res_itype](../iprm_files/iprm_res_itype.md) |
| 24 | fintroduction | 方案介绍 | varchar | 255 |  | √ | ' ' | 方案介绍 |
| 25 | fintroduction_tag | 方案介绍_详情 | text | 0 |  |  | ' ' | 方案介绍_详情 |
| 26 | fbrief | 简介 | varchar | 255 |  | √ | ' ' | 简介 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fcountrytype | 五级国家/地区 | int8 | 64 |  | √ | 0 | [国家/地区 iprm_res_country](../iprm_files/iprm_res_country.md) |
| 29 | fdownloadtimes | 加载次数 | int4 | 32 |  | √ | 0 | 加载次数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iprm_resource_billno |  | fbillno |
| 2 | pk_iprm_resource |  | fid |
