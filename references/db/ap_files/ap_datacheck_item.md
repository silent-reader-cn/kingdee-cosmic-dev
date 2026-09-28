# 数据巡查项-ap_datacheck_item

## 数据巡查项-多语言表 t_ap_datachecksitem_l

- **表名称：** 数据巡查项-多语言表
- **表名：** t_ap_datachecksitem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 巡查项说明 | varchar | 255 |  | √ | ' ' | 巡查项说明 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | ftips | 提示语 | varchar | 255 |  | √ | ' ' | 提示语 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_datachecks_fid |  | fid,flocaleid |
| 2 | pk_t_ap_datachecksitem_l |  | fpkid |

---

## 数据巡查项-主表 t_ap_datachecksitem

- **表名称：** 数据巡查项-主表
- **表名：** t_ap_datachecksitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescription | 巡查项说明 | varchar | 255 |  | √ | ' ' | 巡查项说明 |
| 6 | ftips | 提示语 | varchar | 255 |  | √ | ' ' | 提示语 |
| 7 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fchecktype | 巡查项类型 | varchar | 30 |  | √ | ' ' | 巡查项类型,枚举: plugin :插件 custom :自定义条件 |
| 10 | fcustomfilter | 自定义条件 | varchar | 255 |  | √ | ' ' | 自定义条件 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcustomfilter_tag | 自定义条件_详情 | text | 0 |  |  | null | 自定义条件_详情 |
| 15 | fapp | 应用 | varchar | 30 |  | √ | ' ' | 应用,枚举: ar :应收 ap :应付 |
| 16 | fcustomdesc | 自定义条件描述 | varchar | 255 |  | √ | ' ' | 自定义条件描述 |
| 17 | fcluburl | 社区链接 | varchar | 255 |  | √ | ' ' | 社区链接 |
| 18 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 21 | fbizobj | 巡查对象 | varchar | 30 |  | √ | ' ' | 业务对象 bos_objecttype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_datachecks_fnumber |  | fnumber |
| 2 | pk_t_ap_datachecksitem |  | fid |
