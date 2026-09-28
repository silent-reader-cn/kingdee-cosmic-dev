# 模板配置-pds_noticetpl

## 模板配置-多语言表 t_pds_noticetpl_l

- **表名称：** 模板配置-多语言表
- **表名：** t_pds_noticetpl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_noticetpl_l |  | fpkid |
| 2 | idx_pds_noticetpl_l_fname |  | fname |
| 3 | idx_pds_noticetpl_l_fid |  | fid,flocaleid |

---

## 模板配置-主表 t_pds_noticetpl

- **表名称：** 模板配置-主表
- **表名：** t_pds_noticetpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fbizobject | 业务对象 | varchar | 30 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fcompbizobject | 组件业务对象 | varchar | 30 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fbiztype | 公告类型 | bpchar | 1 |  | √ | ' ' | 公告类型,枚举: 1 :询价公告 C :招标公告 3 :竞价公告 5 :中标公告 6 :招募公告 7 :行业动态 8 :系统公告 A :询价结果公告 B :竞价结果公告 D :流标公告 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcontent_tag | 公告内容_详情 | text | 0 |  |  | null | 公告内容_详情 |
| 16 | ftpltype | 模板类型 | bpchar | 1 |  | √ | '1' | 模板类型,枚举: 1 :公告模板 2 :函件模板 3 :通知模板 4 :采购方标书模板 5 :供应商标书模板 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | fcontent | 公告内容 | varchar | 255 |  | √ | ' ' | 公告内容 |
| 20 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 21 | fnoticecontentplugin | 公告内容解析插件 | varchar | 255 |  | √ | ' ' | 公告内容解析插件 |
| 22 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_noticetpl |  | fid |
| 2 | idx_pds_noticetpl_biz |  | fbizobject |
| 3 | idx_pds_noticetpl_number |  | fnumber |
