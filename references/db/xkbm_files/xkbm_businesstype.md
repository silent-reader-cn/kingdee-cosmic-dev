# 预算业务类型-xkbm_businesstype

## 预算业务类型-主表 t_xkbm_businesstype

- **表名称：** 预算业务类型-主表
- **表名：** t_xkbm_businesstype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [预算业务类型分组 xkbm_businesstypegroup](../xkbm_files/xkbm_businesstypegroup.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fconditionjson | 过滤条件json | varchar | 2000 |  | √ | ' ' | 过滤条件json |
| 7 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | feffectmrpcal | MRP运算项 | varchar | 10 |  | √ | ' ' | MRP运算项,枚举: 0 :MRP输入项 1 :MRP输出项 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fconditionname | 过滤条件 | varchar | 570 |  | √ | ' ' | 过滤条件 |
| 15 | fmuliconditionname | 过滤条件多语言 | varchar | 570 |  | √ | ' ' | 过滤条件多语言 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 18 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 19 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fconditionsql | 过滤条件sql | varchar | 2000 |  | √ | ' ' | 过滤条件sql |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_businesstype |  | fnumber |
| 2 | pk_xkbm_businesstype |  | fid |

---

## 预算业务类型-多语言表 t_xkbm_businesstype_l

- **表名称：** 预算业务类型-多语言表
- **表名：** t_xkbm_businesstype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmuliconditionname | 过滤条件多语言 | varchar | 570 |  | √ | ' ' | 过滤条件多语言 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_businesstype_l |  | fid,flocaleid |
| 2 | pk_xkbm_businesstype_l |  | fpkid |
