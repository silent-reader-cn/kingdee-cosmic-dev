# 库存校验器配置-im_validatorcfg

## 库存校验器配置-主表 t_im_validatorcfg

- **表名称：** 库存校验器配置-主表
- **表名：** t_im_validatorcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 插件描述 | varchar | 255 |  | √ | ' ' | 插件描述 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 6 | fvalidatebill | 校验单据 | varchar | 100 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | floadplugin | 加载插件 | varchar | 255 |  | √ | ' ' | 加载插件 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fquoteplugin | 引用插件 | int8 | 64 |  | √ | 0 | 库存校验器配置 im_validatorcfg |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_validatorcfg_fnumber |  | fnumber |
| 2 | pk_t_im_validatorcfg |  | fid |

---

## 库存校验器配置-多语言表 t_im_validatorcfg_l

- **表名称：** 库存校验器配置-多语言表
- **表名：** t_im_validatorcfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 插件描述 | varchar | 255 |  | √ | ' ' | 插件描述 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_validatorcfg_l |  | fpkid |
| 2 | idx_t_im_validatorcfg_l_id |  | fid,flocaleid |

---

## 校验器信息-子表 t_im_validatorcfgentry

- **表名称：** 校验器信息-子表
- **表名：** t_im_validatorcfgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 3 | fop | 操作 | varchar | 50 |  | √ | ' ' | 操作,枚举: save :保存 submit :提交 audit :审核 delete :删除 unsubmit :撤销 unaudit :反审核 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fimplclass | 实现类 | varchar | 255 |  | √ | ' ' | 实现类 |
| 8 | fisquote | 是否引用 | bpchar | 1 |  | √ | '0' | 是否引用 |
| 9 | fquoteentryid | 引用分录id | int8 | 64 |  | √ | 0 | 引用分录id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_validatorcfgentry |  | fentryid |
| 2 | idx_im_validatorcfgentry_fid |  | fid |

---

## 校验器信息-多语言表 t_im_validatorcfgentry_l

- **表名称：** 校验器信息-多语言表
- **表名：** t_im_validatorcfgentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_validatorcfgentry_l_id |  | fentryid,flocaleid |
| 2 | pk_t_im_validatorcfgentry_l |  | fpkid |
