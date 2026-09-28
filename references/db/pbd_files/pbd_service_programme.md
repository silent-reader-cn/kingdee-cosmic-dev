# 业务调用场景-pbd_service_programme

## 适用组织范围-子表 t_pbd_service_orgentity

- **表名称：** 适用组织范围-子表
- **表名：** t_pbd_service_orgentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompanyorg | 组织名称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fincludesuborg | 包含下级组织 | bpchar | 1 |  | √ | '0' | 包含下级组织 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_service_orgentity |  | fentryid |
| 2 | idx_pbd_servece_org_fid_fseq |  | fid,fseq |

---

## 业务调用场景-多语言表 t_pbd_service_programme_l

- **表名称：** 业务调用场景-多语言表
- **表名：** t_pbd_service_programme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_service_programme_l |  | fpkid |
| 2 | idx_pbd_programme_l_fid |  | fid |

---

## 接口关联设置-子表 t_pbd_service_entryentity

- **表名称：** 接口关联设置-子表
- **表名：** t_pbd_service_entryentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapipurpose | 接口用途 | varchar | 50 |  | √ | ' ' | 接口用途,枚举: A :校验 B :填充 C :展示 D :回调 E :查询 |
| 3 | fstandardapi | 标准接口名称 | int8 | 64 |  | √ | 0 | [接口映射方案 pbd_standard_api](../pbd_files/pbd_standard_api.md) |
| 4 | feffectiveness | 存储时效（天） | int8 | 64 |  | √ | 0 | 存储时效（天） |
| 5 | fplatformapi | 来源接口名称 | int8 | 64 |  | √ | 0 | [外部系统API pbd_extsys_api](../pbd_files/pbd_extsys_api.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_service_entryentity |  | fentryid |
| 2 | idx_pbd_service_entry_fid_fseq |  | fid,fseq |

---

## 业务调用场景-主表 t_pbd_service_programme

- **表名称：** 业务调用场景-主表
- **表名：** t_pbd_service_programme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 4 | fgroupid | 业务场景名称 | int8 | 64 |  | √ | 0 | [业务场景维护 pbd_service_scene](../pbd_files/pbd_service_scene.md) |
| 5 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 6 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fispreinsdata | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 8 | fwholegroup | 集团统一 | bpchar | 1 |  | √ | '0' | 集团统一 |
| 9 | foperator | 业务触发场景 | varchar | 50 |  | √ | ' ' | 业务触发场景,枚举: |
| 10 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | fapplyorg | 适用组织范围 | varchar | 1000 |  | √ | ' ' | 适用组织范围 |
| 12 | ftriggertype | 触发类别 | varchar | 50 |  | √ | ' ' | 触发类别,枚举: A :业务操作 B :条件触发 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | flink | 连接配置方案 | int8 | 64 |  | √ | 0 | [账号配置 pbd_credit_link](../pbd_files/pbd_credit_link.md) |
| 15 | foperatorname | 业务触发场景名称 | varchar | 50 |  | √ | ' ' | 业务触发场景名称 |
| 16 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 21 | fbillentity | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_programme_fmasterid |  | fmasterid |
| 2 | pk_pbd_service_programme |  | fid |
| 3 | idx_pbd_programme_fnumber |  | fnumber |
