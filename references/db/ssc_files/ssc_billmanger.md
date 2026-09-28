# 共享工单管理-ssc_billmanger

## 共享工单管理-主表 t_tk_sscbillmanger

- **表名称：** 共享工单管理-主表
- **表名：** t_tk_sscbillmanger

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 所属分类 | int8 | 64 |  | √ | 0 | 共享工单分类 ssc_billmangerclassify |
| 3 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsourceid | 源集成对象ID | int8 | 64 |  | √ | 0 | 源集成对象ID |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | ftarget_datas | 数据源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fsource_number | 编码 | varchar | 150 |  | √ | ' ' | 编码 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 15 | fentityid | 元数据实体ID | varchar | 15 |  | √ | ' ' | 元数据实体ID |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fname | 名称 | varchar | 60 |  | √ | ' ' | 名称 |
| 18 | fsource_datas | 数据源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 22 | fctrlstrategy | 控制策略 | varchar | 2 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 23 | fsource_name | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 24 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 26 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 27 | ftargetid | 目标集成对象ID | int8 | 64 |  | √ | 0 | 目标集成对象ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tk_sscbillmanger_createorg |  | fcreateorgid |
| 2 | idx_tk_sscbillmanger_no |  | fnumber |
| 3 | idx_t_tk_sscbillmanger_master |  | fmasterid |
| 4 | pk_tk_sscbillmanger |  | fid |

---

## 共享工单管理-使用范围表 t_tk_sscbillmanger_u

- **表名称：** 共享工单管理-使用范围表
- **表名：** t_tk_sscbillmanger_u

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
| 1 | pk_t_tk_sscbillmanger_u |  | fdataid,fuseorgid |
| 2 | idx_t_tk_sscbillmanger_u_uo |  | fuseorgid |

---

## 共享工单管理-多语言表 t_tk_sscbillmanger_l

- **表名称：** 共享工单管理-多语言表
- **表名：** t_tk_sscbillmanger_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 60 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_sscbillmanger_l |  | fpkid |
| 2 | idx_tk_billmanger_l_id |  | fid |

---

## 面板字段属性-多语言表 t_tk_field_subentry_l

- **表名称：** 面板字段属性-多语言表
- **表名：** t_tk_field_subentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffieldname | 字段名称 | varchar | 60 |  | √ | ' ' | 字段名称 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_fieldsubenrty_l_did |  | fdetailid |
| 2 | pk_tk_field_subentry_l |  | fpkid |

---

## 工单面板属性-子表 t_tk_panel_entry

- **表名称：** 工单面板属性-子表
- **表名：** t_tk_panel_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpispreset | 是否预置面板 | bpchar | 1 |  | √ | '0' | 是否预置面板 |
| 3 | fpisvisible | 是否可见面板 | bpchar | 1 |  | √ | '1' | 是否可见面板 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fpnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 6 | fpname | 名称 | varchar | 60 |  | √ | ' ' | 名称 |
| 7 | fptype | 面板类别 | bpchar | 1 |  | √ | '0' | 面板类别,枚举: 0 :单据头 1 :分录 |
| 8 | fpanelid | 面板id | varchar | 15 |  | √ | ' ' | 面板id |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fpcheckmeta | 元数据检查 | bpchar | 1 |  | √ | '0' | 元数据检查,枚举: 0 :未生成元数据 1 :已生成元数据 2 :已提交删除 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_panelentry_id |  | fid |
| 2 | pk_tk_panel_entry |  | fentryid |

---

## 面板字段属性-子表 t_tk_field_subentry

- **表名称：** 面板字段属性-子表
- **表名：** t_tk_field_subentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffcheckmeta | 元数据检查 | bpchar | 1 |  | √ | '0' | 元数据检查,枚举: 0 :未生成元数据 1 :已生成元数据 2 :已提交删除 |
| 2 | ffieldpropertyjson | 字段属性json | varchar | 255 |  | √ | ' ' | 字段属性json |
| 3 | ffieldproperty | 字段属性 | varchar | 500 |  | √ | ' ' | 字段属性 |
| 4 | ffieldname | 字段名称 | varchar | 60 |  | √ | ' ' | 字段名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fismust | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 7 | ffieldapid | 字段控件id | varchar | 15 |  | √ | ' ' | 字段控件id |
| 8 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 9 | fisvisible | 显示 | bpchar | 1 |  | √ | '1' | 显示 |
| 10 | ffieldnumber | 字段编码 | varchar | 30 |  | √ | ' ' | 字段编码 |
| 11 | ffieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型,枚举: Text :单行文本 TextArea :多行文本 LargeText :大文本(blob) Integer :整数 Decimal :小数 Date :日期 DateTime :日期+时间 Basedata :基础资料 Assistant :辅助资料 CheckBox :布尔 Combo :下拉列表 MulCombo :多选下拉列表 Org :组织 Supplier :供应商 User :用户 Customer :客户 Currency :币别 Amount :金额 Materiel :物料 |
| 12 | ffieldpropertyjson_tag | 字段属性json_详情 | text | 0 |  |  | null | 字段属性json_详情 |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_fieldsubentry_eid |  | fentryid |
| 2 | pk_tk_field_subentry |  | fdetailid |
