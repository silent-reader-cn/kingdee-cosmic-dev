# 表内检查公式-xkrpt_verification

## 表内检查公式-多语言表 t_xkrpt_verifyfunc_l

- **表名称：** 表内检查公式-多语言表
- **表名：** t_xkrpt_verifyfunc_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmessage | 审核不满足时显示 | varchar | 255 |  | √ | ' ' | 审核不满足时显示 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_verifyfunc_l |  | fid,flocaleid |
| 2 | pk_xkrpt_verifyfunc_l |  | fpkid |

---

## 单据体-子表 t_xkrpt_verifyfuncctrl

- **表名称：** 单据体-子表
- **表名：** t_xkrpt_verifyfuncctrl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fcontrolstrength | 控制强度 | bpchar | 1 |  | √ | ' ' | 控制强度,枚举: 0 :提示 1 :不通过 |
| 4 | ffuncctrlid | ffuncctrlid | int8 | 64 |  | √ | 0 | id |
| 5 | fcontrolnode | 控制节点 | bpchar | 1 |  | √ | ' ' | 控制节点,枚举: 0 :保存 1 :提交 2 :审核 3 :上报 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | ffuncctrlid | ffuncctrlid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_verifyfuncctrl_id |  | fid |
| 2 | pk_xkrpt_verifyfuncctrl |  | ffuncctrlid |

---

## 表内检查公式-主表 t_xkrpt_verifyfunc

- **表名称：** 表内检查公式-主表
- **表名：** t_xkrpt_verifyfunc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | frptid | 报表 | varchar | 50 |  | √ | ' ' | 报表 |
| 5 | faudittips | 审核提示 | bpchar | 1 |  | √ | '0' | 审核提示,枚举: 0 : 1 :审核-提示 2 :审核-不可审核 |
| 6 | fmessage | 审核不满足时显示 | varchar | 255 |  | √ | ' ' | 审核不满足时显示 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fsheetid | 页签 | varchar | 50 |  | √ | ' ' | 页签 |
| 10 | fgroupsetting | 复选框 | bpchar | 1 |  | √ | ' ' | 复选框 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fsavetips | 保存提示 | bpchar | 1 |  | √ | '0' | 保存提示,枚举: 0 : 1 :保存-提示 |
| 13 | fsubmittips | 提交提示 | bpchar | 1 |  | √ | '0' | 提交提示,枚举: 0 : 1 :提交-提示 2 :提交-不可提交 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fformula | 公式 | varchar | 255 |  | √ | ' ' | 公式 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | freporttips | 上报提示 | bpchar | 1 |  | √ | '0' | 上报提示,枚举: 0 : 1 :上报-提示 2 :上报-不可上报 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_verifyfunc |  | fid |
| 2 | idx_xkrpt_verifyfunc_num |  | fnumber |
