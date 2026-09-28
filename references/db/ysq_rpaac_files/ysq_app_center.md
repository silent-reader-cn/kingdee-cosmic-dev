# RPA应用-ysq_app_center

## RPA应用-主表 tk_ysq_rpa_app_center

- **表名称：** RPA应用-主表
- **表名：** tk_ysq_rpa_app_center

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_ysq_app_use_helper_tag | 使用帮助_详情 | text | 0 |  |  | null | 使用帮助_详情 |
| 3 | fk_ysq_app_group_number | 许可分组id | int8 | 64 |  |  | null | 许可分组id |
| 4 | fk_ysq_app_use_helper | 使用帮助 | varchar | 255 |  | √ | ' ' | 使用帮助 |
| 5 | fk_ysq_launch_date | 上架时间 | timestamp | 0 |  |  | null | 上架时间 |
| 6 | forgid | 组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 8 | fk_ysq_app_label | 应用标签 | varchar | 1024 |  | √ | ' ' | 应用标签 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fk_ysq_app_product_type | 产品线类型 | varchar | 50 |  | √ | ' ' | 产品线类型,枚举: 星瀚 :星瀚 星空旗舰版 :星空旗舰版 |
| 11 | fk_ysq_app_name | 应用机器人名称 | varchar | 256 |  | √ | ' ' | 应用机器人名称 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 15 | fk_ysq_app_involve_sys | 涉及系统 | varchar | 1024 |  | √ | ' ' | 涉及系统 |
| 16 | fk_ysq_app_special | 是否专用 | varchar | 50 |  | √ | ' ' | 是否专用,枚举: yes :是 no :否 |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  |  | null | 原资料id |
| 18 | fbitindex | 位图 | int8 | 64 |  |  | null | 位图 |
| 19 | fk_ysq_app_open_source | 是否开源 | varchar | 50 |  | √ | ' ' | 是否开源,枚举: yes :是 no :否 |
| 20 | fk_ysq_app_permit_code | 许可编号 | varchar | 1024 |  | √ | ' ' | 许可编号 |
| 21 | fk_ysq_app_run_type | 使用权限分类 | varchar | 50 |  |  | '3' | 使用权限分类 |
| 22 | fk_ysq_last_version | 最新版本 | varchar | 256 |  | √ | ' ' | 最新版本 |
| 23 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 24 | fk_ysq_proc_code | 流程编号 | varchar | 32 |  | √ | ' ' | 流程编号 |
| 25 | fk_ysq_app_icon | 应用图标 | varchar | 255 |  | √ | ' ' | 应用图标 |
| 26 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 27 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fk_ysq_update_date | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 30 | fk_ysq_dev_com_code | 开发者公司标识 | varchar | 64 |  | √ | ' ' | 开发者公司标识 |
| 31 | fk_ysq_app_explain | 应用说明 | varchar | 2000 |  | √ | ' ' | 应用说明 |
| 32 | fctrlstrategy | 控制策略 | varchar | 254 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 33 | fk_ysq_app_price | 价格 | numeric | 23 | 2 |  | NULL | 价格 |
| 34 | fk_ysq_app_reserve_tag | 预留字段_详情 | text | 0 |  |  | null | 预留字段_详情 |
| 35 | fk_ysq_dev_com_name | 开发者公司名称 | varchar | 128 |  | √ | ' ' | 开发者公司名称 |
| 36 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 37 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 38 | fk_ysq_app_reserve | 预留字段 | varchar | 255 |  | √ | ' ' | 预留字段 |
| 39 | fsourcebitindex | 原资料位图 | int8 | 64 |  |  | null | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_ysq_rpa_app_center |  | fid |
| 2 | idx_tk_ysq_rpa_app_center_createorg |  | fcreateorgid |
| 3 | idx_tk_ysq_rpa_app_center_master |  | fmasterid |

---

## 附件-附件表 tk_ysq_rpa_app_file

- **表名称：** 附件-附件表
- **表名：** tk_ysq_rpa_app_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | null | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__ysq_rpa_app_file |  | fpkid |

---

## 单据体-子表 tk_ysq_rpa_app_center_ver

- **表名称：** 单据体-子表
- **表名：** tk_ysq_rpa_app_center_ver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_ysq_app_update_content | 更新内容 | varchar | 1024 |  | √ | ' ' | 更新内容 |
| 3 | fk_ysq_app_update_date | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | null | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 6 | fk_ysq_app_ver_code | 版本号 | varchar | 256 |  | √ | ' ' | 版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_ysq_rpa_app_center_ver |  | fentryid |
| 2 | idx__ysq_rpa_app_center_ver_fk |  | fid |

---

## RPA应用-使用范围位图表 tk_ysq_rpa_app_center_m

- **表名称：** RPA应用-使用范围位图表
- **表名：** tk_ysq_rpa_app_center_m

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
| 1 | pk_tk_ysq_rpa_app_center_m |  | forgid |

---

## RPA应用-多语言表 tk_ysq_rpa_app_center_l

- **表名称：** RPA应用-多语言表
- **表名：** tk_ysq_rpa_app_center_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
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
| 1 | pk_tk_ysq_rpa_app_center_l |  | fpkid |
| 2 | idx__ysq_rpa_app_center_l_0 |  | fid,flocaleid |

---

## RPA应用-使用范围表 tk_ysq_rpa_app_center_u

- **表名称：** RPA应用-使用范围表
- **表名：** tk_ysq_rpa_app_center_u

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
| 1 | pk_tk_ysq_rpa_app_center_u |  | fdataid,fuseorgid |
| 2 | idx_tk_ysq_rpa_app_center_u_uo |  | fuseorgid |
