# 质检服务-qcbd_triggerset

## 质检服务-多语言表 t_qcbd_triggerset_l

- **表名称：** 质检服务-多语言表
- **表名：** t_qcbd_triggerset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_trigetl_fname |  | fname |
| 2 | pk_qcbd_triggerset_l |  | fpkid |
| 3 | idx_qcbd_trigetl_fid |  | fid,flocaleid |

---

## 配置详情-子表 t_qcbd_triggersetentry

- **表名称：** 配置详情-子表
- **表名：** t_qcbd_triggersetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fmethodname | 微服务方法名 | varchar | 50 |  | √ | ' ' | 微服务方法名 |
| 4 | fcloudid | 云ID | varchar | 50 |  | √ | ' ' | 云ID |
| 5 | fclassname | 微服务类名 | varchar | 50 |  | √ | ' ' | 微服务类名 |
| 6 | ftriggerscene | 触发场景 | varchar | 5 |  | √ | ' ' | 触发场景,枚举: A :控制性校验 B :业务反写 |
| 7 | ftriggerenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | ftriggermode | 触发方式 | varchar | 5 |  | √ | ' ' | 触发方式,枚举: A :微服务 B :外部系统API |
| 10 | ftrigger | 触发时机 | varchar | 5 |  | √ | ' ' | 触发时机,枚举: A :审核 B :反审核 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fappid | 应用ID | varchar | 50 |  | √ | ' ' | 应用ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_trigry_fid |  | fid |
| 2 | idx_qcbd_trigry_fseq |  | fseq |
| 3 | pk_qcbd_triggersetentry |  | fentryid |

---

## 质检服务-主表 t_qcbd_triggerset

- **表名称：** 质检服务-主表
- **表名：** t_qcbd_triggerset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | ftriggerobjid | 触发实体对象 | varchar | 255 |  | √ | '0' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | ftargetobjid | 目标实体对象 | varchar | 255 |  | √ | '0' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fissysy | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_triget_fnumber |  | fnumber |
| 2 | pk_qcbd_triggerset |  | fid |
| 3 | idx_qcbd_triget_fcreatetime |  | fcreatetime |
