# 体系管理1（废弃）-fpm_bodysysmanage

## 体系管理1（废弃）-多语言表 t_fpm_bodysysmanage_l

- **表名称：** 体系管理1（废弃）-多语言表
- **表名：** t_fpm_bodysysmanage_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fcomment | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_bodysysmanage_l |  | fpkid |
| 2 | idx_fpm_bodysysmanage_l |  | fid |

---

## 体系管理1（废弃）-主表 t_fpm_bodysysmanage

- **表名称：** 体系管理1（废弃）-主表
- **表名：** t_fpm_bodysysmanage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatormanage | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 责任组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 7 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 16 | fcurrencyid | 责任组织本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 17 | fratetype | 折算汇率类型 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_bodysysmanage |  | fid |
| 2 | idx_fpm_bodysysmanage |  | fnumber |

---

## 适用编报类型-子表 t_fpm_bodysysmanage_type

- **表名称：** 适用编报类型-子表
- **表名：** t_fpm_bodysysmanage_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fissumreport | 是否汇总上报 | bpchar | 1 |  | √ | '0' | 是否汇总上报 |
| 3 | frollnumber | 滚动期数 | int4 | 32 |  | √ | 0 | 滚动期数 |
| 4 | frereporttypestatus | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: enable :可用 disable :禁用 |
| 5 | fiscontaindetail | 滚动期是否含明细期间 | bpchar | 1 |  | √ | '0' | 滚动期是否含明细期间 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fismodify | 汇总级是否可修改 | bpchar | 1 |  | √ | '0' | 汇总级是否可修改 |
| 9 | frerporttype | 编报类型 | int8 | 64 |  | √ | 0 | [编报类型设置（废弃） fpm_orgreporttype](../fpm_files/fpm_orgreporttype.md) |
| 10 | fisroll | 是否滚动 | bpchar | 1 |  | √ | '0' | 是否滚动 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpm_bodysysmanage_type |  | fid |
| 2 | pk_t_fpm_bodysysmanage_type |  | fentryid |

---

## 用户组-多选基础资料表 t_fpm_bodysysmanage_ug

- **表名称：** 用户组-多选基础资料表
- **表名：** t_fpm_bodysysmanage_ug

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [收付认领用户组 fbd_usergroup](../fbd_files/fbd_usergroup.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fpm_bodysysmanage_ug |  | fid |
| 2 | pk_t_fpm_bodysysmanage_ug |  | fpkid |

---

## 单据体-子表 t_fpm_bodysysmanage_mang

- **表名称：** 单据体-子表
- **表名：** t_fpm_bodysysmanage_mang

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmanagertypebdtype | 多选基础资料类型 | varchar | 50 |  | √ | ' ' | 多选基础资料类型,枚举: bos_user :用户 fbd_usergroup :用户组 |
| 3 | fmanager | 用户组/用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fmanagertype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: curruser :创建人 bos_user :用户 bos_usergroup :用户组 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_bodysysmanage_mang |  | fentryid |
| 2 | idx_fpm_bodysysmanage_mang |  | fid |

---

## 用户-多选基础资料表 t_fpm_bodysysmanage_user

- **表名称：** 用户-多选基础资料表
- **表名：** t_fpm_bodysysmanage_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_bodysysmanage_user |  | fpkid |
| 2 | idx_t_fpm_bodysysmanage_user |  | fid |
