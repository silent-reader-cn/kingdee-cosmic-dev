# 轻量级扩展-bos_lightlayout

## 单据体-子表 t_bas_lightlayoutlist

- **表名称：** 单据体-子表
- **表名：** t_bas_lightlayoutlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flistvif7 | 列表F7界面可见 | bpchar | 1 |  | √ | '0' | 列表F7界面可见 |
| 3 | fseq | 分录行号 | int2 | 16 |  | √ | 0 | 分录行号 |
| 4 | flistkey | 列表字段标识 | varchar | 50 |  | √ | ' ' | 列表字段标识 |
| 5 | flistdspname | 列表显示名称 | varchar | 255 |  | √ | ' ' | 列表显示名称 |
| 6 | flistviinit | 列表缺省可见 | bpchar | 1 |  | √ | '0' | 列表缺省可见 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | flistlayouttype | 列表终端类型 | varchar | 50 |  | √ | ' ' | 列表终端类型 |
| 9 | flistcontrolid | 列表控件ID | varchar | 50 |  | √ | ' ' | 列表控件ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_lightlayoutlist |  | fentryid |
| 2 | ix_t_bas_lightlayoutlist_id |  | fid |

---

## 表单设置_保存-子表 t_bas_lightlayoutbill

- **表名称：** 表单设置_保存-子表
- **表名：** t_bas_lightlayoutbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontrolid | 控件Id | varchar | 50 |  | √ | ' ' | 控件Id |
| 3 | ffielddefvalue | 缺省值 | varchar | 255 |  | √ | ' ' | 缺省值 |
| 4 | ffielddefvaluedesign | 缺省值设计时 | varchar | 500 |  | √ | ' ' | 缺省值设计时 |
| 5 | flocknew | 新增锁定 | bpchar | 1 |  | √ | '0' | 新增锁定 |
| 6 | fviview | 查看可见 | bpchar | 1 |  | √ | '0' | 查看可见 |
| 7 | fvisubmit | 提交可见 | bpchar | 1 |  | √ | '0' | 提交可见 |
| 8 | fseq | 分录行号 | int2 | 16 |  | √ | 0 | 分录行号 |
| 9 | flockmodify | 修改锁定 | bpchar | 1 |  | √ | '0' | 修改锁定 |
| 10 | ftreenodeid | 树节点Id | varchar | 50 |  | √ | ' ' | 树节点Id |
| 11 | ffieldid | 字段Id | varchar | 50 |  | √ | ' ' | 字段Id |
| 12 | ffieldkey | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 13 | fviaudit | 审核可见 | bpchar | 1 |  | √ | '0' | 审核可见 |
| 14 | fviinit | 初始可见 | bpchar | 1 |  | √ | '0' | 初始可见 |
| 15 | fvinew | 新增可见 | bpchar | 1 |  | √ | '0' | 新增可见 |
| 16 | ffielddspname | 显示名称 | varchar | 255 |  | √ | ' ' | 显示名称 |
| 17 | flocksubmit | 提交锁定 | bpchar | 1 |  | √ | '0' | 提交锁定 |
| 18 | flockaudit | 审核锁定 | bpchar | 1 |  | √ | '0' | 审核锁定 |
| 19 | fvimodify | 修改可见 | bpchar | 1 |  | √ | '0' | 修改可见 |
| 20 | ffieldmustinput | 是否必录 | bpchar | 1 |  | √ | '0' | 是否必录 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ix_t_bas_lightlayoutbill_id |  | fid |
| 2 | pk_t_bas_lightlayoutbill |  | fentryid |

---

## 轻量级扩展-主表 t_bas_lightlayout

- **表名称：** 轻量级扩展-主表
- **表名：** t_bas_lightlayout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | flayouttype | 表单终端 | varchar | 50 |  | √ | ' ' | 表单终端,枚举: pc :PC端 mobile :移动端 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: BaseFormModel :基础资料 BillFormModel :单据 Layout :布局 |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
| 13 | flistlayouttype | 列表终端 | varchar | 50 |  | √ | ' ' | 列表终端,枚举: pc :PC端 mobile :移动端 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_lightlayout |  | fid |
| 2 | ix_bas_lightlayout_number |  | fnumber |

---

## 轻量级扩展-多语言表 t_bas_lightlayout_l

- **表名称：** 轻量级扩展-多语言表
- **表名：** t_bas_lightlayout_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_lightlayout_l_fid |  | fid,flocaleid |
| 2 | pk_t_bas_lightlayout_l |  | fpkid |

---

## 表单设置_保存-多语言表 t_bas_lightlayoutbill_l

- **表名称：** 表单设置_保存-多语言表
- **表名：** t_bas_lightlayoutbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffielddspname | 显示名称 | varchar | 255 |  | √ | ' ' | 显示名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_lightlayoutbill_l |  | fpkid |
| 2 | idx_bas_lightlayoutbill_l_fid |  | fentryid,flocaleid |

---

## 单据体-多语言表 t_bas_lightlayoutlist_l

- **表名称：** 单据体-多语言表
- **表名：** t_bas_lightlayoutlist_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | flistdspname | 列表显示名称 | varchar | 255 |  | √ | ' ' | 列表显示名称 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_lightlayoutlist_l_fid |  | fentryid,flocaleid |
| 2 | pk_t_bas_lightlayoutlist_l |  | fpkid |
