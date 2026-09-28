# 我的RPA应用-ysq_app_mine

## 我的RPA应用-主表 tk_ysq_rpa_app_mine

- **表名称：** 我的RPA应用-主表
- **表名：** tk_ysq_rpa_app_mine

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | forgid | 组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 3 | fk_ysq_lic_status | 许可状态 | varchar | 50 |  | √ | ' ' | 许可状态,枚举: 0 :过期 1 :有效 |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 5 | fk_ysq_app_label | 应用标签 | varchar | 1024 |  | √ | ' ' | 应用标签 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fk_ysq_app_name | 应用机器人名称 | varchar | 256 |  | √ | ' ' | 应用机器人名称 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 11 | fk_ysq_app_involve_sys | 涉及系统 | varchar | 1024 |  | √ | ' ' | 涉及系统 |
| 12 | fk_ysq_app_use_help | 使用帮助 | varchar | 255 |  | √ | ' ' | 使用帮助 |
| 13 | fk_ysq_app_special | 是否专用 | varchar | 50 |  | √ | ' ' | 是否专用,枚举: yes :是 no :否 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  |  | null | 原资料id |
| 15 | fbitindex | 位图 | int8 | 64 |  |  | null | 位图 |
| 16 | fk_ysq_app_open_source | 是否开源 | varchar | 50 |  | √ | ' ' | 是否开源,枚举: yes :是 no :否 |
| 17 | fk_ysq_app_run_type | 使用权限分类 | varchar | 50 |  |  | '3' | 使用权限分类 |
| 18 | fk_ysq_last_version | 机器人版本 | varchar | 256 |  | √ | ' ' | 机器人版本 |
| 19 | fk_ysq_app_use_help_tag | 使用帮助_详情 | text | 0 |  |  | null | 使用帮助_详情 |
| 20 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 21 | fk_ysq_proc_code | 流程编号 | varchar | 32 |  | √ | ' ' | 流程编号 |
| 22 | fk_ysq_app_icon | 应用图标 | varchar | 255 |  | √ | ' ' | 应用图标 |
| 23 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 25 | fk_ysq_end_date | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fk_ysq_update_date | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 28 | fk_ysq_dev_com_code | 开发者公司标识 | varchar | 64 |  | √ | ' ' | 开发者公司标识 |
| 29 | fk_ysq_app_explain | 应用说明 | varchar | 2000 |  | √ | ' ' | 应用说明 |
| 30 | fctrlstrategy | 控制策略 | varchar | 254 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 31 | fk_ysq_app_price | 价格 | numeric | 23 | 2 |  | NULL | 价格 |
| 32 | fk_ysq_start_date | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 33 | fk_ysq_dev_com_name | 开发者公司名称 | varchar | 128 |  | √ | ' ' | 开发者公司名称 |
| 34 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 35 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 36 | fsourcebitindex | 原资料位图 | int8 | 64 |  |  | null | 原资料位图 |
| 37 | fk_ysq_status | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: Activated :已导入 noActivated :未导入 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_ysq_rpa_app_mine |  | fid |
| 2 | idx_tk_ysq_rpa_app_mine_master |  | fmasterid |
| 3 | idx_tk_ysq_rpa_app_mine_createorg |  | fcreateorgid |

---

## 我的RPA应用-使用范围表 tk_ysq_rpa_app_mine_u

- **表名称：** 我的RPA应用-使用范围表
- **表名：** tk_ysq_rpa_app_mine_u

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
| 1 | idx_tk_ysq_rpa_app_mine_u_uo |  | fuseorgid |
| 2 | pk_tk_ysq_rpa_app_mine_u |  | fdataid,fuseorgid |

---

## 我的RPA应用-多语言表 tk_ysq_rpa_app_mine_l

- **表名称：** 我的RPA应用-多语言表
- **表名：** tk_ysq_rpa_app_mine_l

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
| 1 | idx__ysq_rpa_app_mine_l_0 |  | fid,flocaleid |
| 2 | pk_tk_ysq_rpa_app_mine_l |  | fpkid |

---

## 我的RPA应用-使用范围位图表 tk_ysq_rpa_app_mine_m

- **表名称：** 我的RPA应用-使用范围位图表
- **表名：** tk_ysq_rpa_app_mine_m

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
| 1 | pk_tk_ysq_rpa_app_mine_m |  | forgid |

---

## 单据体-子表 tk_ysq_rpa_app_mine_ver

- **表名称：** 单据体-子表
- **表名：** tk_ysq_rpa_app_mine_ver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_ysq_app_update_content | 更新内容 | varchar | 1024 |  | √ | ' ' | 更新内容 |
| 3 | fk_ysq_app_update_date | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | null | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 6 | fk_ysq_app_ver_code | 版本编号 | varchar | 256 |  | √ | ' ' | 版本编号 |
| 7 | fk_ysq_fk_proc_code | 流程编号 | varchar | 32 |  | √ | ' ' | 流程编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__ysq_rpa_app_mine_ver_fk |  | fid |
| 2 | pk_tk_ysq_rpa_app_mine_ver |  | fentryid |
