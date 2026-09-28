# 管控维度-pbd_controldimension

## 管控维度-主表 t_pbd_controldimension

- **表名称：** 管控维度-主表
- **表名：** t_pbd_controldimension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbasedatatypeid | 基础资料 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 7 | ffieldname | 基础资料属性 | varchar | 255 |  | √ | ' ' | 基础资料属性,枚举: |
| 8 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 9 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 10 | fpluginparams | 插件参数 | varchar | 255 |  | √ | ' ' | 插件参数 |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fdimensiontype | 维度类型 | bpchar | 1 |  | √ | ' ' | 维度类型,枚举: 1 :基础资料 2 :基础资料属性 3 :插件取值 |
| 17 | fissys | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fplugin | 取值插件 | varchar | 255 |  | √ | ' ' | 取值插件 |
| 20 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_dimension_fbasedataid |  | fbasedatatypeid |
| 2 | pk_t_pbd_controldimension |  | fid |

---

## 管控维度-多语言表 t_pbd_controldimension_l

- **表名称：** 管控维度-多语言表
- **表名：** t_pbd_controldimension_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pbd_controldimension_l |  | fpkid |
| 2 | idx_pbd_controldimension_l_fid |  | fid,flocaleid |
