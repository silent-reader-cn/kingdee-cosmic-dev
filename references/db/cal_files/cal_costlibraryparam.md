# 成本库配置参数-cal_costlibraryparam

## 成本库匹配信息-子表 t_cal_clpruleentry

- **表名称：** 成本库匹配信息-子表
- **表名：** t_cal_clpruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostlibname | 成本库字段名称 | varchar | 50 |  | √ | ' ' | 成本库字段名称 |
| 3 | fsrcbillname | 业务单字段名称 | varchar | 50 |  | √ | ' ' | 业务单字段名称 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fsrcbillfield | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fcostlibfield | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_clpruleentry_fid |  | fid |
| 2 | pk_t_cal_clpruleentry |  | fentryid |

---

## 适用组织信息-子表 t_cal_clporgentry

- **表名称：** 适用组织信息-子表
- **表名：** t_cal_clporgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostaccount | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 3 | forgfield | 适用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cal_clporgentry |  | fentryid |
| 2 | t_cal_clporgentry_fid |  | fid |

---

## 成本价类型-多选基础资料表 t_cal_costparam_costtype

- **表名称：** 成本价类型-多选基础资料表
- **表名：** t_cal_costparam_costtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [成本价类型 cal_costlibrarytype](../cal_files/cal_costlibrarytype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costparam_costtype_fid |  | fid |
| 2 | pk_t_cal_costparam_costtype |  | fpkid |

---

## 成本库配置参数-多语言表 t_cal_costlibraryparam_l

- **表名称：** 成本库配置参数-多语言表
- **表名：** t_cal_costlibraryparam_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
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
| 1 | pk_cal_costlibraryparam_l |  | fpkid |
| 2 | t_cal_costlibraryparam_l_fid |  | fid |

---

## 字段映射-子表 t_cal_clpmapentry

- **表名称：** 字段映射-子表
- **表名：** t_cal_clpmapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcefield | 业务单字段标识 | varchar | 255 |  | √ | ' ' | 业务单字段标识 |
| 3 | fsourcefieldname | 业务单字段名称 | varchar | 50 |  | √ | ' ' | 业务单字段名称 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fcostfieldname | 成本库字段名称 | varchar | 50 |  | √ | ' ' | 成本库字段名称 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fcostfield | 成本库字段标识 | varchar | 50 |  | √ | ' ' | 成本库字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_clpmapentry_fid |  | fid |
| 2 | pk_t_cal_clpmapentry |  | fentryid |

---

## 成本库配置参数-主表 t_cal_costlibraryparam

- **表名称：** 成本库配置参数-主表
- **表名：** t_cal_costlibraryparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | forgfield | 适用组织字段标识 | varchar | 50 |  | √ | ' ' | 适用组织字段标识 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ffilter_tag | 过滤条件_详情 | text | 0 |  |  | null | 过滤条件_详情 |
| 7 | fdatefield | 记账日期字段标识 | varchar | 50 |  | √ | ' ' | 记账日期字段标识 |
| 8 | fwritetype | 反写价格类型 | int8 | 64 |  | √ | 0 | [成本价类型 cal_costlibrarytype](../cal_files/cal_costlibrarytype.md) |
| 9 | fsourcebill | 业务单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fmulcosttype | 价格类型（废弃） | varchar | 50 |  | √ | ' ' | 价格类型（废弃）,枚举: beginunit :期初加权价 unitcost :加权平均价 endunit :期末加权价 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | ffilter | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costlibraryparam_source |  | fsourcebill |
| 2 | pk_t_cal_costlibraryparam |  | fid |
