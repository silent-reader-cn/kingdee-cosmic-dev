# 维度成员映射（废弃）-fpm_dimensionmember

## 维度成员映射（废弃）-主表 t_fpm_dimensionmember

- **表名称：** 维度成员映射（废弃）-主表
- **表名：** t_fpm_dimensionmember

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseassistbasedata | 是否使用辅助业务基础资料 | bpchar | 1 |  | √ | '0' | 是否使用辅助业务基础资料 |
| 3 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 5 | fassistbizbasedata | 辅助业务基础资料 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdimensionid | 维度 | int8 | 64 |  | √ | 0 | [维度（废弃） fpm_dimension](../fpm_files/fpm_dimension.md) |
| 8 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 9 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 10 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fbizbasedata | 业务基础资料 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | fbodysysmanage | 体系 | int8 | 64 |  | √ | 0 | [体系管理1（废弃） fpm_bodysysmanage](../fpm_files/fpm_bodysysmanage.md) |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 20 | fdimension | fdimension | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_dimensionmember |  | fid |
| 2 | idx_fpm_dimensionmember |  | fnumber |

---

## 维度成员映射（废弃）-多语言表 t_fpm_dimensionmember_l

- **表名称：** 维度成员映射（废弃）-多语言表
- **表名：** t_fpm_dimensionmember_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
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
| 1 | idx_fpm_dimensionmember_l |  | fid |
| 2 | pk_t_fpm_dimensionmember_l |  | fpkid |

---

## 成员映射关系-子表 t_fpm_dimensionmember_ent

- **表名称：** 成员映射关系-子表
- **表名：** t_fpm_dimensionmember_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizbasedatadetail | 业务基础资料 | varchar | 50 |  | √ | ' ' | 业务基础资料 |
| 3 | fbizbasedatadetailid | 业务基础资料id | int8 | 64 |  | √ | 0 | 业务基础资料id |
| 4 | fbizbdrange | 业务基础资料范围 | varchar | 50 |  | √ | ' ' | 业务基础资料范围,枚举: sublevel :所有下级 onlyself :仅自己 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fassistbasedatadetailid | 辅助业务基础资料id | int8 | 64 |  | √ | 0 | 辅助业务基础资料id |
| 7 | fdimmembercode | fdimmembercode | varchar | 50 |  | √ | ' ' |  |
| 8 | fassistbasedatadetailcode | 辅助业务基础资料编码 | varchar | 50 |  | √ | ' ' | 辅助业务基础资料编码 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fassistbasedatadetail | 辅助业务基础资料 | varchar | 50 |  | √ | ' ' | 辅助业务基础资料 |
| 11 | fbizbasedatadetailcode | 业务基础资料编码 | varchar | 50 |  | √ | ' ' | 业务基础资料编码 |
| 12 | fdimmember | 维度成员 | int8 | 64 |  | √ | 0 | [维度成员模板（废弃） fpm_member](../fpm_files/fpm_member.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fpm_dimensionmember_ent |  | fentryid |
| 2 | idx_fpm_dimensionmember_ent |  | fid |
