# 工作台卡片配置-pbd_todoconfig

## 工作台卡片配置-多语言表 t_pbd_todoconfig_l

- **表名称：** 工作台卡片配置-多语言表
- **表名：** t_pbd_todoconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 卡片名称 | varchar | 100 |  | √ | ' ' | 卡片名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_todoconfig_l |  | fpkid |
| 2 | idx_pbd_todoconfig_l_fid |  | fid |

---

## 单据体-子表 t_pbd_todoconfigentry

- **表名称：** 单据体-子表
- **表名：** t_pbd_todoconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftabstatusid | 页签状态 | int8 | 64 |  | √ | 0 | 工作台待办页签状态 pbd_todostatus |
| 3 | fclassname | 取数插件 | varchar | 255 |  | √ | ' ' | 取数插件 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentityid | 业务对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_todocfgentry_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_todoconfigentry |  | fentryid |

---

## 工作台卡片配置-主表 t_pbd_todoconfig

- **表名称：** 工作台卡片配置-主表
- **表名：** t_pbd_todoconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 卡片名称 | varchar | 20 |  | √ | ' ' | 卡片名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fgroupid | 所属应用 | varchar | 36 |  | √ | ' ' | 业务应用列表 bos_devp_bizapplist |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ficon_selected | 卡片选中图标 | varchar | 255 |  | √ | ' ' | 卡片选中图标 |
| 7 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | ficon | 卡片默认图标 | varchar | 255 |  | √ | ' ' | 卡片默认图标 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcardseq | 卡片序号 | int4 | 32 |  | √ | 0 | 卡片序号 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 卡片编码 | varchar | 80 |  | √ | ' ' | 卡片编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_todoconfig |  | fid |
| 2 | idx_pbd_todo_config_fnumber |  | fnumber |
| 3 | idx_pbd_todo_config_fmasterid |  | fmasterid |
