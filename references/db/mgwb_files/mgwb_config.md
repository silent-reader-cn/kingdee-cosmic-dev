# 移动星空工作台配置-mgwb_config

## 移动星空工作台配置-多语言表 t_mgwb_config_l

- **表名称：** 移动星空工作台配置-多语言表
- **表名：** t_mgwb_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 230 |  | √ | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fbillname | 名称 | varchar | 230 |  | √ | ' ' | 名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mgwb_config_l |  | fpkid |
| 2 | idx_mgwb_config_l_idloc |  | fid,flocaleid |

---

## 自建表单显示-多语言表 t_mgwb_configentry_l

- **表名称：** 自建表单显示-多语言表
- **表名：** t_mgwb_configentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fnickname | 显示名称 | varchar | 230 |  | √ | ' ' | 显示名称 |
| 5 | fgroupname | fgroupname | varchar | 230 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mgwb_configentry_lidloc |  | fentryid,flocaleid |
| 2 | pk_mgwb_configentry_l |  | fpkid |

---

## 自建表单显示-子表 t_mgwb_configentry

- **表名称：** 自建表单显示-子表
- **表名：** t_mgwb_configentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillformid | 移动列表 | varchar | 36 |  | √ | ' ' | 移动列表 |
| 3 | fenableform | 启用新增 | bpchar | 1 |  | √ | ' ' | 启用新增 |
| 4 | fmobileformid | 移动表单 | varchar | 36 |  | √ | ' ' | 移动表单 |
| 5 | fmodeltype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: BillFormModel :单据 BaseFormModel :基础资料 MobileFormModel :移动表单 MobileBillFormModel :移动单据 |
| 6 | fenablelist | 启用列表 | bpchar | 1 |  | √ | ' ' | 启用列表 |
| 7 | fmetaid | 名称 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fnickname | 显示名称 | varchar | 230 |  | √ | ' ' | 显示名称 |
| 11 | fformid | 标识 | varchar | 36 |  | √ | ' ' | 标识 |
| 12 | fgroupname | fgroupname | varchar | 230 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mgwb_configentry |  | fentryid |
| 2 | idx_mgwb_configentry_fid |  | fid |

---

## 分录单据体-多语言表 t_mgwb_appentry_l

- **表名称：** 分录单据体-多语言表
- **表名：** t_mgwb_appentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fappviewname | 显示名称 | varchar | 100 |  | √ | ' ' | 显示名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mgwb_appentry_l |  | fentryid,flocaleid |
| 2 | pk_t_mgwb_appentry_l |  | fpkid |

---

## 分级应用组-多语言表 t_mgwb_configappgroup_l

- **表名称：** 分级应用组-多语言表
- **表名：** t_mgwb_configappgroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fappgroupdesc | 应用组描述 | varchar | 2000 |  |  | ' ' | 应用组描述 |
| 2 | fappgroupname | 应用组名称 | varchar | 50 |  | √ | ' ' | 应用组名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mgwb_configappgroup_l |  | fpkid |
| 2 | idx_mgwb_configappgroup_lidloc |  | fentryid,flocaleid |

---

## 分级应用组-子表 t_mgwb_configappgroup

- **表名称：** 分级应用组-子表
- **表名：** t_mgwb_configappgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fappgroupdesc | 应用组描述 | varchar | 2000 |  |  | ' ' | 应用组描述 |
| 3 | fappgroupname | 应用组名称 | varchar | 50 |  | √ | ' ' | 应用组名称 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mgwb_configappgroup |  | fentryid |
| 2 | idx_mgwb_configappgroup_fid |  | fid |

---

## 轻应用显示-多语言表 t_mgwb_configappentry_l

- **表名称：** 轻应用显示-多语言表
- **表名：** t_mgwb_configappentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fappnickname | 显示名称 | varchar | 230 |  | √ | ' ' | 显示名称 |
| 2 | fappname | fappname | varchar | 230 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mgwb_configappentry_l |  | fpkid |
| 2 | idx_mgwb_configappentry_lid |  | fentryid,flocaleid |

---

## 轻应用显示-子表 t_mgwb_configappentry

- **表名称：** 轻应用显示-子表
- **表名：** t_mgwb_configappentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fappnickname | 显示名称 | varchar | 230 |  | √ | ' ' | 显示名称 |
| 3 | fappname | fappname | varchar | 230 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fappimage | 图标 | varchar | 255 |  | √ | ' ' | 图标 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fappid | 应用标识 | int8 | 64 |  | √ | 0 | [轻应用 mbase_lightapp](../mbase_files/mbase_lightapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mgwb_configappentry_fid |  | fid |
| 2 | pk_mgwb_configappentry |  | fentryid |

---

## 移动星空工作台配置-主表 t_mgwb_config

- **表名称：** 移动星空工作台配置-主表
- **表名：** t_mgwb_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 7 | fdescription | 描述 | varchar | 230 |  | √ | ' ' | 描述 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbillno | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 10 | fbillname | 名称 | varchar | 230 |  | √ | ' ' | 名称 |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mgwb_config_status |  | fenable,fbillstatus |
| 2 | pk_mgwb_config |  | fid |
| 3 | idx_mgwb_config_billno |  | fbillno |

---

## 分录单据体-子表 t_mgwb_appentry

- **表名称：** 分录单据体-子表
- **表名：** t_mgwb_appentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgroupid | 分组ID | int8 | 64 |  | √ | 0 | 分组ID |
| 3 | fappnumber | 应用编码 | int8 | 64 |  | √ | 0 | [移动实体 mbase_mobentity](../mbase_files/mbase_mobentity.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fappviewname | 显示名称 | varchar | 100 |  | √ | ' ' | 显示名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mgwb_appentry |  | fentryid |
| 2 | idx_t_mgwb_appentry_fid |  | fid |
