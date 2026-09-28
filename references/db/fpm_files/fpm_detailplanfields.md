# 明细计划字段（废弃）-fpm_detailplanfields

## 明细计划字段（废弃）-主表 t_fpm_detailplanfields

- **表名称：** 明细计划字段（废弃）-主表
- **表名：** t_fpm_detailplanfields

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ffieldname | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 6 | fismustinput | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 7 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 8 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 9 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fdetaildimtype | 明细维度类型 | varchar | 50 |  | √ | ' ' | 明细维度类型,枚举: |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsyssetpre | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 16 | fsort | 排序字段 | int4 | 32 |  | √ | 0 | 排序字段 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 20 | fbodysys | 体系 | int8 | 64 |  | √ | 0 | [体系管理1（废弃） fpm_bodysysmanage](../fpm_files/fpm_bodysysmanage.md) |
| 21 | foption | 选项 | varchar | 255 |  | √ | ' ' | 选项 |
| 22 | fdatatype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: |
| 23 | fisshow | 可见 | bpchar | 1 |  | √ | '0' | 可见 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_detailplanfields |  | fid |
| 2 | idx_t_fpm_detailplanfields |  | fbodysys |

---

## 明细计划字段（废弃）-多语言表 t_fpm_detailplanfields_l

- **表名称：** 明细计划字段（废弃）-多语言表
- **表名：** t_fpm_detailplanfields_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 显示名称 | varchar | 50 |  | √ | ' ' | 显示名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fpm_detailplanfields_l |  | fid |
| 2 | pk_t_fpm_detailplanfields_l |  | fpkid |
