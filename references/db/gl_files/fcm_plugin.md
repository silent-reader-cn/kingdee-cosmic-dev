# 检查项插件-fcm_plugin

## 检查项插件-多语言表 t_fcm_checkingplugin_l

- **表名称：** 检查项插件-多语言表
- **表名：** t_fcm_checkingplugin_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 功能描述 | varchar | 512 |  | √ | ' ' | 功能描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fcm_checkingplugin_l |  | fid,flocaleid |
| 2 | pk_t_fcm_checkingplugin_l |  | fpkid |

---

## 检查项插件-使用范围位图表 t_fcm_checkingplugin_m

- **表名称：** 检查项插件-使用范围位图表
- **表名：** t_fcm_checkingplugin_m

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
| 1 | pk_t_fcm_checkingplugin_m |  | forgid |

---

## 检查项插件-使用范围表 t_fcm_checkingplugin_u

- **表名称：** 检查项插件-使用范围表
- **表名：** t_fcm_checkingplugin_u

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
| 1 | idx_t_fcm_checkingplugin_u_uo |  | fuseorgid |
| 2 | pk_t_fcm_checkingplugin_u |  | fdataid,fuseorgid |

---

## 单据体-多语言表 t_fcm_pluginparamentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_fcm_pluginparamentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fpvaluerange | 有效值范围 | varchar | 512 |  | √ | ' ' | 有效值范围 |
| 2 | fpname | 参数名称 | varchar | 50 |  | √ | ' ' | 参数名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpdesc | 参数描述 | varchar | 512 |  | √ | ' ' | 参数描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcm_pluginparamentry_l |  | fpkid |
| 2 | idx_fcm_ppel_entryid |  | fentryid,flocaleid |

---

## 单据体-子表 t_fcm_pluginparamentry

- **表名称：** 单据体-子表
- **表名：** t_fcm_pluginparamentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpcode | 参数编码 | varchar | 50 |  | √ | ' ' | 参数编码 |
| 3 | fpdefaultvalue | 参数默认值 | varchar | 20 |  | √ | ' ' | 参数默认值 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | fpvaluerange | fpvaluerange | varchar | 512 |  | √ | ' ' |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fpname | fpname | varchar | 50 |  | √ | ' ' |  |
| 8 | fptype | 参数类型 | varchar | 10 |  | √ | ' ' | 参数类型,枚举: text :文本 boolean :布尔 int :整形 combo :下拉框 basedata :基础资料 |
| 9 | fpdesc | fpdesc | varchar | 512 |  | √ | ' ' |  |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fprequire | 必填 | bpchar | 1 |  | √ | ' ' | 必填 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcm_pluginparamentry |  | fentryid |
| 2 | idx_fcm_ppe_id |  | fid |
| 3 | idx_fcm_ppe_createtime |  | fcreatetime |

---

## 检查项插件-主表 t_fcm_checkingplugin

- **表名称：** 检查项插件-主表
- **表名：** t_fcm_checkingplugin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '6' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fapplicationid | 应用 | varchar | 20 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 18 | fchecktypeid | 类型 | varchar | 20 |  | √ | ' ' | 类型,枚举: |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fdesc | 功能描述 | varchar | 512 |  | √ | ' ' | 功能描述 |
| 21 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fcm_checkingplugin_master |  | fmasterid |
| 2 | pk_t_fcm_checkingplugin |  | fid |
| 3 | idx_fcm_cp_fnumber |  | fnumber |
| 4 | idx_t_fcm_checkingplugin_createorg |  | fcreateorgid |
