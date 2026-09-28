# 巡检检查项-xkcts_inspectitem

## 巡检检查项-多语言表 t_xkinsp_item_l

- **表名称：** 巡检检查项-多语言表
- **表名：** t_xkinsp_item_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | ffixtips | 修复建议 | varchar | 500 |  | √ | ' ' | 修复建议 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | ftips | 提示 | varchar | 200 |  | √ | ' ' | 提示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkinsp_item_l |  | fpkid |
| 2 | idx_xkinsp_item_l |  | fid,flocaleid |

---

## 执行插件分录-子表 t_xkinsp_itemexec

- **表名称：** 执行插件分录-子表
- **表名：** t_xkinsp_itemexec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftypeid | 分类 | int8 | 64 |  | √ | 0 | [巡检插件分类 xkcts_inspectplugintype](../cts_files/xkcts_inspectplugintype.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fenable | 是否启用 | varchar | 1 |  | √ | '1' | 是否启用 |
| 6 | fpath | 路径 | varchar | 200 |  | √ | ' ' | 路径 |
| 7 | fdescription | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkinsp_itemexec |  | fentryid |
| 2 | idx_itemexec_fid |  | fid,fseq |

---

## 巡检检查项-主表 t_xkinsp_item

- **表名称：** 巡检检查项-主表
- **表名：** t_xkinsp_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffixmethod | 异常修复方式 | bpchar | 1 |  | √ | ' ' | 异常修复方式,枚举: 1 :自动 2 :手工 |
| 3 | ftips | 提示 | varchar | 200 |  | √ | ' ' | 提示 |
| 4 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 5 | fappid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcustomfilter | 后台检查条件（不可见） | varchar | 255 |  | √ | ' ' | 后台检查条件（不可见） |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcustomfilter_tag | 后台检查条件（不可见）_详情 | text | 0 |  |  | ' ' | 后台检查条件（不可见）_详情 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcheckmode | 检查配置 | bpchar | 1 |  | √ | ' ' | 检查配置,枚举: 1 :自定义 2 :插件 |
| 13 | ffixtips | 修复建议 | varchar | 500 |  | √ | ' ' | 修复建议 |
| 14 | fissystem | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 15 | fwarnlevel | 控制级别 | varchar | 50 |  | √ | ' ' | 控制级别,枚举: 200 :弱控制 300 :强控制 |
| 16 | fitemtypeid | 巡检分类 | int8 | 64 |  | √ | 0 | [巡检业务分类 xkcts_inspectitemtype](../cts_files/xkcts_inspectitemtype.md) |
| 17 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fobjectid | 检查对象 | int8 | 64 |  | √ | 0 | [巡检业务对象 xkcts_inspectobject](../cts_files/xkcts_inspectobject.md) |
| 21 | finspecttype | 检查类型 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 22 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 23 | feffective | 生效状态 | bpchar | 1 |  | √ | '1' | 生效状态,枚举: 0 :失效 1 :生效 |
| 24 | fenable | 可用状态 | bpchar | 1 |  | √ | '0' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkinsp_item |  | fid |
| 2 | idx_xkinsp_item_type |  | fitemtypeid |

---

## 修复插件分录-子表 t_xkinsp_itemrepair

- **表名称：** 修复插件分录-子表
- **表名：** t_xkinsp_itemrepair

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftypeid | 分类 | int8 | 64 |  | √ | 0 | [巡检插件分类 xkcts_inspectplugintype](../cts_files/xkcts_inspectplugintype.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fenable | 是否启用 | varchar | 1 |  | √ | '1' | 是否启用 |
| 6 | fpath | 路径 | varchar | 200 |  | √ | ' ' | 路径 |
| 7 | fdescription | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_itemrepair_fid |  | fid,fseq |
| 2 | pk_xkinsp_itemrepair |  | fentryid |
