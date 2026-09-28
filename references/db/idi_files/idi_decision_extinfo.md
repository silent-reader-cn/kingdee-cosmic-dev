# 检查项扩展-idi_decision_extinfo

## 检查项扩展-多语言表 t_idi_decisionextinfo_l

- **表名称：** 检查项扩展-多语言表
- **表名：** t_idi_decisionextinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_idi_decisionextinfo_l |  | fpkid |
| 2 | idx_idi_decisionextinfo_l_fid |  | fid |

---

## 检查项扩展-主表 t_idi_decisionextinfo

- **表名称：** 检查项扩展-主表
- **表名：** t_idi_decisionextinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmethodname | 接口名 | varchar | 80 |  | √ | ' ' | 接口名 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fservice_type | 微服务类别 | varchar | 10 |  | √ | ' ' | 微服务类别,枚举: BOS :平台 BIZ :业务 ISV :二开 |
| 5 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fpluginclass | 插件类名 | varchar | 200 |  | √ | ' ' | 插件类名 |
| 8 | fdetaildisplaytype | 辅助信息展示样式 | bpchar | 1 |  | √ | '0' | 辅助信息展示样式,枚举: 0 :悬停 1 :下拉 |
| 9 | fissysset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 10 | fmethodparams_tag | 接口参数json_详情 | text | 0 |  |  | null | 接口参数json_详情 |
| 11 | fmethodparams | 接口参数json | varchar | 255 |  | √ | ' ' | 接口参数json |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fappid | 应用ID | varchar | 50 |  | √ | ' ' | 应用ID |
| 14 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fext_type | 扩展类型 | varchar | 20 |  | √ | ' ' | 扩展类型,枚举: MSERVICE :微服务 PLUGIN :插件 |
| 18 | fcloudid | 云ID | varchar | 50 |  | √ | ' ' | 云ID |
| 19 | fservicename | 微服务名 | varchar | 80 |  | √ | ' ' | 微服务名 |
| 20 | fsrcentitynum | 源单（已废弃） | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 23 | fdesc | 说明 | varchar | 255 |  | √ | ' ' | 说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_idi_decisionextinfo_src |  | fsrcentitynum |
| 2 | pk_t_idi_decisionextinfo |  | fid |
| 3 | idx_idi_decisionextinfo_num |  | fnumber |

---

## 源单-多选基础资料表 t_idi_decisionextentry

- **表名称：** 源单-多选基础资料表
- **表名：** t_idi_decisionextentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_idi_decisionextentry_fk |  | fid |
| 2 | pk_t_idi_decisionextentry |  | fpkid |
