# 影像超时提醒规则-bas_imageremind

## 影像超时提醒规则-主表 t_bas_imageremind

- **表名称：** 影像超时提醒规则-主表
- **表名：** t_bas_imageremind

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcalendartype | 日历类型 | bpchar | 1 |  | √ | '1' | 日历类型,枚举: 1 :自然日历 2 :工作日历 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fpriority | 优先级 | varchar | 10 |  | √ | ' ' | 优先级 |
| 6 | fnoticescene | 消息通知场景 | varchar | 10 |  | √ | ',1,' | 消息通知场景,枚举: 1 :影像就绪 2 :影像重传 |
| 7 | fremindcycle | 提醒周期（天） | int8 | 64 |  | √ | 0 | 提醒周期（天） |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fmessageobject | 消息对象 | varchar | 10 |  | √ | ' ' | 消息对象,枚举: 0 :经办人 1 :扫描岗 |
| 13 | fmessagechannel | 消息渠道 | varchar | 10 |  | √ | ' ' | 消息渠道,枚举: 1 :云之家 3 :邮件 4 :短信 5 :钉钉 |
| 14 | fmessagetitle | fmessagetitle | varchar | 1000 |  | √ | ' ' |  |
| 15 | fexpiredday | 超期天数 | int8 | 64 |  | √ | 0 | 超期天数 |
| 16 | fmessagetemplate | fmessagetemplate | varchar | 1000 |  | √ | ' ' |  |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编号 | varchar | 50 |  | √ | ' ' | 编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_imageremind |  | fid |
| 2 | index_bas_imageremind |  | fenable |

---

## 影像超时提醒规则-多语言表 t_bas_imageremind_l

- **表名称：** 影像超时提醒规则-多语言表
- **表名：** t_bas_imageremind_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmessagetitle | 消息标题 | varchar | 1000 |  | √ | ' ' | 消息标题 |
| 4 | fmessagetemplate | 消息模板 | varchar | 1000 |  | √ | ' ' | 消息模板 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_imageremind_l_pkey |  | fpkid |
| 2 | index_t_bas_imageremind_l |  | flocaleid |

---

## 单据-多选基础资料表 t_bas_imageremindbill

- **表名称：** 单据-多选基础资料表
- **表名：** t_bas_imageremindbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 100 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_t_bas_imageremindbill |  | fbasedataid |
| 2 | t_bas_imageremindbill_pkey |  | fpkid |

---

## 消息渠道-多选基础资料表 t_bas_imageexpire_channel

- **表名称：** 消息渠道-多选基础资料表
- **表名：** t_bas_imageexpire_channel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [消息渠道 msg_channel](../wftask_files/msg_channel.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_imagechannel_fid |  | fid |
| 2 | pk_bas_imageexpire_channel |  | fpkid |

---

## 组织-多选基础资料表 t_bas_imageremindorg

- **表名称：** 组织-多选基础资料表
- **表名：** t_bas_imageremindorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_imageremindorg_pkey |  | fpkid |
| 2 | index_t_bas_imageremindorg |  | fbasedataid |
