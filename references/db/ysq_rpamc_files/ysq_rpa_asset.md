# 变量管理-ysq_rpa_asset

## 变量管理-主表 tk_ysq_rpa_asset

- **表名称：** 变量管理-主表
- **表名：** tk_ysq_rpa_asset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_ysq_org_sel | 所属业务组织 | varchar | 50 |  | √ | ' ' | 所属业务组织,枚举: |
| 3 | fk_ysq_robots_no | 机器人编号 -all- -deptall- -机器人唯一标识- 多个英文,隔开 | varchar | 255 |  | √ | ' ' | 机器人编号 -all- -deptall- -机器人唯一标识- 多个英文,隔开 |
| 4 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fk_useorg | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fk_ysq_is_client_edit | 客户端可修改 yes 是 no 否 | bpchar | 1 |  | √ | '0' | 客户端可修改 yes 是 no 否 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fk_ysq_agent_alias_tag | 机器人别名 -all- -deptall- -别名- 多个英文,隔开_详情 | text | 0 |  | √ | ' ' | 机器人别名 -all- -deptall- -别名- 多个英文,隔开_详情 |
| 11 | fk_ysq_is_python_expr | 保存为python类型 | bpchar | 1 |  | √ | '0' | 保存为python类型 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  |  | null | 原资料id |
| 15 | fbitindex | 位图 | int8 | 64 |  |  | null | 位图 |
| 16 | fk_ysq_robots_no_tag | 机器人编号 -all- -deptall- -机器人唯一标识- 多个英文,隔开_详情 | text | 0 |  | √ | ' ' | 机器人编号 -all- -deptall- -机器人唯一标识- 多个英文,隔开_详情 |
| 17 | fk_ysq_robots_no_sel | 机器人下拉选项 | varchar | 2000 |  | √ | ' ' | 机器人下拉选项,枚举: |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fctrlstrategy | 控制策略 | varchar | 254 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 23 | fk_ysq_asset_value | 变量值 | varchar | 255 |  | √ | ' ' | 变量值 |
| 24 | fk_ysq_asset_value_tag | 变量值_详情 | text | 0 |  | √ | ' ' | 变量值_详情 |
| 25 | fk_ysq_asset_type | 变量类型 text：文本 passwd：密码 | varchar | 50 |  | √ | ' ' | 变量类型 text：文本 passwd：密码,枚举: text :文本 passwd :密码 |
| 26 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | fk_ysq_agent_alias | 机器人别名 -all- -deptall- -别名- 多个英文,隔开 | varchar | 255 |  | √ | ' ' | 机器人别名 -all- -deptall- -别名- 多个英文,隔开 |
| 29 | fsourcebitindex | 原资料位图 | int8 | 64 |  |  | null | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_ysq_rpa_asset |  | fid |
| 2 | idx_tk_ysq_rpa_asset_master |  | fmasterid |
| 3 | idx_tk_ysq_rpa_asset_createorg |  | fcreateorgid |

---

## 变量管理-使用范围表 tk_ysq_rpa_asset_u

- **表名称：** 变量管理-使用范围表
- **表名：** tk_ysq_rpa_asset_u

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
| 1 | idx_tk_ysq_rpa_asset_u_uo |  | fuseorgid |
| 2 | pk_tk_ysq_rpa_asset_u |  | fdataid,fuseorgid |

---

## 变量管理-多语言表 tk_ysq_rpa_asset_l

- **表名称：** 变量管理-多语言表
- **表名：** tk_ysq_rpa_asset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fk_ysq_asset_name | 变量名称 | varchar | 128 |  | √ | ' ' | 变量名称 |
| 4 | fk_ysq_asset_desc | 变量描述 | varchar | 256 |  | √ | ' ' | 变量描述 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__ysq_rpa_asset_l_0 |  | fid,flocaleid |
| 2 | pk_tk_ysq_rpa_asset_l |  | fpkid |

---

## 变量管理-使用范围位图表 tk_ysq_rpa_asset_m

- **表名称：** 变量管理-使用范围位图表
- **表名：** tk_ysq_rpa_asset_m

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
| 1 | pk_tk_ysq_rpa_asset_m |  | forgid |
