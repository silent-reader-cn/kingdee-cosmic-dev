# 数据巡检模型-msbd_inspectunit

## 数据巡检模型-多语言表 t_msbd_inspectunit_l

- **表名称：** 数据巡检模型-多语言表
- **表名：** t_msbd_inspectunit_l

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
| 1 | pk_t_msbd_inspectunit_l |  | fpkid |
| 2 | idx_msbd_inspectunit_l_fid |  | fid,flocaleid |
| 3 | idx_msbd_inspectunit_l_fname |  | fname,fid |

---

## 校验条件实体-子表 t_msbd_inspectunitentry_v

- **表名称：** 校验条件实体-子表
- **表名：** t_msbd_inspectunitentry_v

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvaliddescription | 描述说明 | varchar | 1000 |  |  | null | 描述说明 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fvalidenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 6 | fvalidjson_tag | 校验条件json_详情 | text | 0 |  |  | null | 校验条件json_详情 |
| 7 | fvalidjson | 校验条件json | varchar | 1000 |  |  | null | 校验条件json |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msbd_inspectunitentry_v |  | fentryid |
| 2 | idx_msbd_inspectunitentry_v |  | fid |

---

## 执行服务-子表 t_msbd_inspectunitentry_m

- **表名称：** 执行服务-子表
- **表名：** t_msbd_inspectunitentry_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmsmethodname | 方法名称 | varchar | 200 |  |  | null | 方法名称 |
| 3 | fbizcloud | 业务云 | varchar | 200 |  |  | null | 业务云 |
| 4 | fmsname | 微服务名称 | varchar | 200 |  |  | null | 微服务名称 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fmsenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fmsimplclass | 微服务实现类 | varchar | 200 |  |  | null | 微服务实现类 |
| 9 | fbizappid | 业务应用 | varchar | 200 |  |  | null | 业务应用实体 bos_devportal_bizapp |
| 10 | fmsparameterarray | 参数数组JSON | varchar | 1000 |  |  | null | 参数数组JSON |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_inspectunitentry_m |  | fid |
| 2 | pk_t_msbd_inspectunitentry_m |  | fentryid |

---

## 处理插件实体-子表 t_msbd_inspectunitentry_p

- **表名称：** 处理插件实体-子表
- **表名：** t_msbd_inspectunitentry_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustomparameter_tag | 自定义参数_详情 | text | 0 |  |  | null | 自定义参数_详情 |
| 3 | fpluginenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 4 | fplugindescription | 描述说明 | varchar | 1000 |  |  | null | 描述说明 |
| 5 | fpluginjson | 插件JSON | varchar | 1000 |  |  | null | 插件JSON |
| 6 | fpluginclassname | 插件名称 | varchar | 200 |  |  | null | 插件名称 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fpluginclassurl | 插件路径 | varchar | 200 |  |  | null | 插件路径 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fcustomparameter | 自定义参数 | varchar | 512 |  |  | null | 自定义参数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_inspectunitentry_p |  | fid |
| 2 | pk_t_msbd_inspectunitentry_p |  | fentryid |

---

## 数据巡检模型-主表 t_msbd_inspectunit

- **表名称：** 数据巡检模型-主表
- **表名：** t_msbd_inspectunit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fareajson | 数据范围条件json | varchar | 512 |  |  | null | 数据范围条件json |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fareajson_tag | 数据范围条件json_详情 | text | 0 |  |  | null | 数据范围条件json_详情 |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fdataqualitystandard | 数据质量标准 | varchar | 5 |  | √ | 'C' | 数据质量标准,枚举: C :数据准确性 B :数据一致性 A :数据唯一性 D :数据关联性 E :数据完整性 F :数据及时性 |
| 10 | fdescription | fdescription | varchar | 512 |  |  | null |  |
| 11 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fareadescription | 条件描述 | varchar | 2000 |  |  | null | 条件描述 |
| 17 | fbizlink | 业务链接 | bpchar | 1 |  | √ | '0' | 业务链接 |
| 18 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fwarnlevel | 告警级别 | varchar | 5 |  | √ | ' ' | 告警级别,枚举: A :一般 B :警告 C :严重 |
| 20 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 21 | fentityid | 单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 22 | fpartitionsql | 分割SQL字段 | varchar | 255 |  | √ | ' ' | 分割SQL字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msbd_inspectunit |  | fid |
| 2 | idx_msbd_inspectunit_fnumber |  | fnumber |
