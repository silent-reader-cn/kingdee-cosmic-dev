# 请求服务定义-pbd_servicedefine

## 请求服务定义-多语言表 t_pbd_servicedefine_l

- **表名称：** 请求服务定义-多语言表
- **表名：** t_pbd_servicedefine_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 40 |  | √ | ' ' |  |
| 2 | fname | 服务名称 | varchar | 255 |  | √ | ' ' | 服务名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_servicedefine_l |  | fid,flocaleid |
| 2 | pk_pbd_servicedefine_l |  | fpkid |

---

## 请求服务定义-主表 t_pbd_servicedefine

- **表名称：** 请求服务定义-主表
- **表名：** t_pbd_servicedefine

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fname | 服务名称 | varchar | 512 |  | √ | ' ' | 服务名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fserviceargsclass | 服务参数类 | varchar | 255 |  | √ | ' ' | 服务参数类 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fimplementation | 服务实现 | varchar | 255 |  | √ | ' ' | 服务实现 |
| 9 | fnumber | 服务编码 | varchar | 80 |  | √ | ' ' | 服务编码 |
| 10 | fconfigform | 服务配置页面 | varchar | 80 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 11 | fservicetype | 服务类型 | varchar | 80 |  | √ | ' ' | 服务类型,枚举: isc :集成云服务 mservice :微服务 opeation :执行操作 plugin :执行插件 api :API接口 custom :自定义 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_pbd_servicedefine |  | fid |
| 2 | idx_pbd_servicedefine_fnumber |  | fnumber |
