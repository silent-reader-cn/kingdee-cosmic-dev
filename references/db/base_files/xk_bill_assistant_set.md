# 制单助手配置-xk_bill_assistant_set

## 制单助手配置-多语言表 t_xkbill_assistant_set_l

- **表名称：** 制单助手配置-多语言表
- **表名：** t_xkbill_assistant_set_l

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
| 1 | idx_t_xkbill_assistant_set_id |  | fid |
| 2 | pk_t_xkbill_assistant_set_l |  | fpkid |

---

## 制单助手配置-主表 t_xkbill_assistant_set

- **表名称：** 制单助手配置-主表
- **表名：** t_xkbill_assistant_set

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | favatarpath | 图标路径 | varchar | 100 |  | √ | ' ' | 图标路径 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fctrlkey | 自定义控件标识 | varchar | 100 |  | √ | ' ' | 自定义控件标识 |
| 6 | fassistantid | 助手ID | varchar | 100 |  | √ | ' ' | 助手ID |
| 7 | fshowstyle | 显示样式 | varchar | 100 |  | √ | ' ' | 显示样式,枚举: floatAboveTheContainer :悬浮页面右侧 embeddedToTheContainer :嵌入到页面容器中 smallPopupWindow :小弹窗 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | flocation | 展示位置 | varchar | 100 |  | √ | ' ' | 展示位置,枚举: TOP :顶部 RIGHT :右侧 LEFT :左侧 BOTTOM :底部 |
| 10 | fshowkey | 展示标识 | varchar | 100 |  | √ | ' ' | 展示标识 |
| 11 | fwidth | 宽度 | int4 | 32 |  | √ | 0 | 宽度 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fflow | 任务流 | varchar | 100 |  | √ | ' ' | [任务流 gai_process](../gai_files/gai_process.md) |
| 18 | fheight | 高度 | int4 | 32 |  | √ | 0 | 高度 |
| 19 | fclickhidectrl | 点击空白处隐藏控件 | bpchar | 1 |  | √ | '0' | 点击空白处隐藏控件 |
| 20 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 21 | fbizobjnumber | 业务对象编码 | varchar | 100 |  | √ | ' ' | 业务对象编码 |
| 22 | fbizobj | 业务对象 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_xkbill_assistant_setnum |  | fbizobjnumber |
| 2 | pk_t_xkbill_assistant_set |  | fid |
