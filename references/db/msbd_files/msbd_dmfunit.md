# 操作校验单元-msbd_dmfunit

## 操作校验单元-主表 t_msbd_dmfunit

- **表名称：** 操作校验单元-主表
- **表名：** t_msbd_dmfunit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 4 | fareajson | 数据范围条件json | varchar | 512 |  |  | null | 数据范围条件json |
| 5 | fscopetype | 处理类型 | varchar | 5 |  | √ | ' ' | 处理类型,枚举: JY :操作校验 JC :数据巡查 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fareajson_tag | 数据范围条件json_详情 | text | 0 |  |  | null | 数据范围条件json_详情 |
| 8 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 9 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 10 | fdescription | fdescription | varchar | 512 |  |  | null |  |
| 11 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fareadescription | 条件描述 | varchar | 2000 |  |  | null | 条件描述 |
| 17 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fentityid | 单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_dmfunit_fnumber |  | fnumber |
| 2 | pk_t_msbd_dmfunit |  | fid |

---

## 处理插件实体-子表 t_msbd_dmfunitentry_p

- **表名称：** 处理插件实体-子表
- **表名：** t_msbd_dmfunitentry_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustomparameter_tag | 自定义参数_详情 | varchar | 512 |  |  | null | 自定义参数_详情 |
| 3 | fpluginenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 4 | fplugindescription | 描述说明 | varchar | 1000 |  |  | null | 描述说明 |
| 5 | fpluginjson | 插件JSON | varchar | 1000 |  |  | null | 插件JSON |
| 6 | fpluginclassname | 插件名称 | varchar | 200 |  |  | null | 插件名称 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fpluginclassurl | 插件路径 | varchar | 200 |  |  | null | 插件路径 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fcustomparameter | 自定义参数 | text | 0 |  |  | null | 自定义参数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_dmfunitentry_p |  | fid |
| 2 | pk_t_msbd_dmfunitentry_p |  | fentryid |

---

## 校验条件实体-子表 t_msbd_dmfunitentry_v

- **表名称：** 校验条件实体-子表
- **表名：** t_msbd_dmfunitentry_v

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvaliddescription | 描述说明 | varchar | 1000 |  |  | null | 描述说明 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fvalidenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 6 | fvalidjson_tag | 校验条件json_详情 | text | 0 |  |  | null | 校验条件json_详情 |
| 7 | fvalidjson | 校验条件json | varchar | 512 |  |  | null | 校验条件json |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_dmfunitentry_v |  | fid |
| 2 | pk_t_msbd_dmfunitentry_v |  | fentryid |

---

## 操作校验单元-多语言表 t_msbd_dmfunit_l

- **表名称：** 操作校验单元-多语言表
- **表名：** t_msbd_dmfunit_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_dmfunit_l_fname |  | fname,fid |
| 2 | idx_msbd_dmfunit_l_fid |  | fid,flocaleid |
| 3 | pk_t_msbd_dmfunit_l |  | fpkid |
